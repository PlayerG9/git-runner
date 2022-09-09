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


from . import process  # noqa
from . import auth  # noqa


@api.get('/test')
async def test():
    return {"Hello": "World"}


# "hidden" endpoint because why not
@api.get('coffee', include_in_schema=False)
async def coffee():
    raise fastapi.HTTPException(
        status_code=fastapi.status.HTTP_418_IM_A_TEAPOT,
        detail="Server refuses to brew coffee because it is a teapot."
    )
