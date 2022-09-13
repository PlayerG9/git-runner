#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sqlalchemy.orm


engine = sqlalchemy.create_engine('sqlite:///database.sl3', echo=True)


BaseModel = sqlalchemy.orm.declarative_base()


def initDatabase():
    BaseModel.metadata.create_all(bind=engine)


class _MetaSession(sqlalchemy.orm.Session):
    def __enter__(self) -> sqlalchemy.orm.Session: ...


def createSession() -> _MetaSession:
    return _MetaSession(bind=engine)
