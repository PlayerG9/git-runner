#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os.path
import fastapi


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
    return fastapi.responses.FileResponse(webResource('index.html'))


@website.get(
    '/{path:path}',
    include_in_schema=False
)
async def getFile(path: str = fastapi.Path()):
    return fastapi.responses.FileResponse(webResource(path))


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
