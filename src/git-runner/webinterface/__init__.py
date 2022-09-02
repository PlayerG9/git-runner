#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os.path
import fastapi
from fastapi.responses import FileResponse


website = fastapi.APIRouter()

RESOURCE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'website'
    )
)


@website.get(
    '/',
    include_in_schema=False
)
async def getIndex():
    return FileResponse(webResource('index.html'))


@website.get(
    '/{path:path}',
    include_in_schema=False
)
async def getFile(path: str = fastapi.Path()):
    if os.path.splitext(path)[1]:
        return FileResponse(webResource('index.html'))  # support for front-end based routing (e.g. react-router)
    filepath = webResource(path)
    if os.path.isdir(filepath):
        filepath = webResource(path, 'index.html')
    if not os.path.isfile(filepath):
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail="file not found"
        )
    return FileResponse(filepath)


def webResource(*path: str):
    final = os.path.abspath(
        os.path.join(
            RESOURCE_PATH,
            *path
        )
    )
    if os.path.commonpath([final, RESOURCE_PATH]) != RESOURCE_PATH:
        raise FileNotFoundError()
    return final
