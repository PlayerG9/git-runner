#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

__version__ = (0, 1, 0)
__version_str__ = '.'.join(str(v) for v in __version__)

api = fastapi.FastAPI(
    title="Git-Runner",
    version=__version_str__,
)
api.add_middleware(CORSMiddleware)
# api.add_middleware(HTTPSRedirectMiddleware)
api.add_middleware(GZipMiddleware)


from . import process_stats  # noqa
from . import auth  # noqa


@api.get('/test')
async def test():
    return {"Hello": "World"}
