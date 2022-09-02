#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi


api = fastapi.APIRouter(prefix='/api')


from . import process_stats  # noqa
from . import auth  # noqa


@api.get('/test')
async def test():
    return {"Hello": "World"}
