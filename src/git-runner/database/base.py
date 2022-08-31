#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import sqlalchemy
import sqlalchemy.orm


engine = sqlalchemy.create_engine('sqlite:///database.sl3', echo=True)


BaseModel = sqlalchemy.orm.declarative_base()


def initDatabase():
    BaseModel.metadata.create_all(bind=engine)


def createSession():
    return sqlalchemy.orm.sessionmaker(bind=engine)
