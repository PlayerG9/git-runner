#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
from . import models as m
from . import base


def getOrCreateAuth(username: str) -> m.Authentication:
    with base.createSession() as session:
        result = session.query(m.Authentication).filter(m.Authentication.username == username).one_or_none()

        if result is None:
            result = m.Authentication(username=username)
            session.add(result)
            session.commit()
            session.refresh(result)
    return result


def deleteAuth(token: str):
    with base.createSession() as session:
        session.query().filter(m.Authentication.auth_key == token).delete()


def verifyApiKey(token: str) -> bool:
    with base.createSession() as session:
        auth = session.query(m.Authentication.auth_key).filter(m.Authentication.auth_key == token).one_or_none()
        return auth is not None
