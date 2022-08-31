#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import typing as t
import requests
import schedule
import database
from database import models as m


class Data:
    pass


@schedule.every().minute.do
def update():
    logging.info("Update github-webhooks")


def getRepositories() -> t.List[str]:
    with database.createSession() as session:
        data = session.query(m.GithubRepository.repository_url).all()
    return [d[0] for d in data]
