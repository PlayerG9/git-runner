#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi.security
import database
from utility import login
from .. import api
from . import models


@fastapi.Depends
def auth(token: str = fastapi.Depends(fastapi.security.APIKeyHeader(name="api-key"))):
    if not database.crud.verifyApiKey(token=token):
        raise PermissionError("invalid api-key")
    return token


auth_router = fastapi.APIRouter(
    prefix="/auth",
    tags=["authentication"],
)


@auth_router.get(
    '/token',
    response_model=models.TokenResponse
)
async def getToken(credentials: fastapi.security.HTTPBasicCredentials = fastapi.Depends(fastapi.security.HTTPBasic())):
    r"""
    get the api-token for the user
    """
    login.verify_login(username=credentials.username, password=credentials.password)
    authentication = database.crud.getOrCreateAuth(username=credentials.username)
    return models.TokenResponse(
        token=authentication.auth_key
    )


@auth_router.get(
    '/reset',
    response_model=models.TokenResponse
)
async def getReset(token: str = auth):
    r"""
    reset the api-token (logs out on all devices)
    """
    database.crud.deleteAuth(token=token)
    return {}


@auth_router.get(
    '/verify',
    response_model=models.VerifyResponse
)
async def getVerify(token: str = auth):
    r"""
    simply verify if the current token is valid
    """
    return dict(
        success=True,
        token=token
    )


api.include_router(auth_router)
