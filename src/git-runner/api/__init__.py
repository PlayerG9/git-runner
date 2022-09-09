#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from . import util

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


@api.exception_handler(Exception)
async def exceptionHandler(request: fastapi.Request, exception: Exception):
    if isinstance(exception, fastapi.HTTPException):
        status = exception.status_code
        detail = exception.detail
    else:
        status = 500
        detail = str(exception)
    message, description = util.status2info(exception.status_code)
    return dict(
        status=status,
        message=message,
        description=description,
        detail=detail
    )


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
