#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
from api import api as api_router
from webhook import webhook as webhook_router
from webinterface import website as website_router

app = fastapi.FastAPI()

app.include_router(api_router)
app.include_router(webhook_router)
app.include_router(website_router)
