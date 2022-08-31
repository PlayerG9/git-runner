#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
from pprint import pprint


webhook = fastapi.APIRouter()


@webhook.post('/github-webhook')
async def endpoint(data: dict = fastapi.Body()):
    pprint(data)
