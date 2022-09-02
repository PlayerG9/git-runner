#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import pyconfig  # noqa (configures python and libraries)
import fastapi
import fastapi.middleware.cors as cors
# import fastapi.middleware.gzip as gzip
from api import api as api_router
from webinterface import website as website_router
import update_checker  # noqa
import database

__version__ = (0, 1, 0)
__version_str__ = '.'.join(str(v) for v in __version__)

app = fastapi.FastAPI(
    title="Git-Runner",
    version=__version_str__,
)
app.add_middleware(cors.CORSMiddleware)
# app.add_middleware(gzip.GZipMiddleware)

app.include_router(api_router)
app.include_router(website_router)

database.initialiseDatabase()
