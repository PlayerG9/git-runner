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
    return FileResponse(webResource(path))


def webResource(path: str):
    final = os.path.abspath(
        os.path.join(
            RESOURCE_PATH,
            path
        )
    )
    if os.path.commonpath([final, RESOURCE_PATH]) != RESOURCE_PATH:
        raise FileNotFoundError()
    return final
