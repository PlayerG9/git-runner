#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from pydantic import BaseModel


class TokenResponse(BaseModel):
    token: str


class VerifyResponse(BaseModel):
    success: bool = True
    token: str
