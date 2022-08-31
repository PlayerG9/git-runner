#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi


api = fastapi.APIRouter(prefix='/api')


@api.get('/test')
async def test():
    return {"Hello": "World"}
