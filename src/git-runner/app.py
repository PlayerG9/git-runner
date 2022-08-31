#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
import pyconfig  # noqa (configures python and libraries)
from api import api as api_router
from webinterface import website as website_router
import update_checker  # noqa
import database

app = fastapi.FastAPI()

app.include_router(api_router)
app.include_router(website_router)

database.initialiseDatabase()
