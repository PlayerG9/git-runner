#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from .base import BaseModel
import sqlalchemy as sql


class GithubRepository(BaseModel):
    __tablename__ = 'github-repositories'

    id = sql.Column(sql.Integer(), primary_key=True)
    repository_url = sql.Column(sql.String())
    command = sql.Column(sql.String())
    pid = sql.Column(sql.String())
