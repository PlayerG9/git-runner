#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
from pprint import pprint
from . import github_updater # noqa (registers a schedule)


webhook = fastapi.APIRouter()


@webhook.post('/github-webhook')
async def endpoint(data: dict = fastapi.Body()):
    pprint(data)
