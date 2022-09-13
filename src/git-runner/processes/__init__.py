#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import psutil

import database
import database.models as dbm
from . import crud


def initialiseProcesses():
    session = database.createSession()
    with session:
        repos = session.query(dbm.GithubRepository).filter(not dbm.GithubRepository.disabled).all()

    with session:
        for repo in repos:
            try:
                crud.stopProcess(repo.pid)
            except psutil.NoSuchProcess:
                pass
            pid = crud.startProcess(repository=repo)
            session.query().filter(dbm.GithubRepository.repository == repo.repository).update({'pid': pid})
