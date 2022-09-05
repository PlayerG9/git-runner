#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import pyconfig  # noqa (configures python and libraries)
import fastapi
from fastapi.staticfiles import StaticFiles

import utility
from api import api as api_app


app = fastapi.FastAPI(
    openapi_url=None,
    docs_url=None,
    redoc_url=None
)


app.mount('/api', api_app)
app.mount('/', StaticFiles(directory=utility.local('website'), html=True))


@app.exception_handler(404)
async def custom404handler(request: fastapi.Request, exception: Exception):
    file_handler: StaticFiles = request.scope.get('endpoint', None)
    if isinstance(file_handler, StaticFiles):
        # github-pages like 404.html option
        custom404file = file_handler.lookup_path('404.html')[0]
        if custom404file:
            return file_handler.get_response(path=custom404file, scope=request.scope)

    return fastapi.responses.FileResponse(utility.local('utility', '404.html'))
