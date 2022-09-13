#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import uuid
import sqlalchemy as sql
from .base import BaseModel


class GithubRepository(BaseModel):
    __tablename__ = 'github-repositories'

    repository = sql.Column(sql.String(), primary_key=True, unique=True)
    command = sql.Column(sql.String())
    pid = sql.Column(sql.String(), nullable=True)
    disabled = sql.Column(sql.Boolean())


class Authentication(BaseModel):
    __tablename__ = 'auth-keys'

    username = sql.Column(sql.String(), primary_key=True, unique=True)
    auth_key = sql.Column(sql.String(32), default=lambda: uuid.uuid1().hex)
