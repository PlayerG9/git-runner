#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os

import fastapi
import psutil

import database
from database import models as dbm
from .. import api
from .. import auth
from . import models
import processes.crud as processes

process_router = fastapi.APIRouter(
    prefix="/process",
    tags=["process"],
    dependencies=[auth.auth]  # noqa
)


@process_router.get(
    '/info/{git-user}/{repo-name}',
    response_model=models.ProcessInfoResponse
)
async def getInfo(git_user: str, repo_name: str):
    r"""
    get information about a process
    """
    repo = f"{git_user}/{repo_name}"
    with database.createSession() as session:
        pid = session.query(dbm.GithubRepository.pid).filter(dbm.GithubRepository.repository == repo).scalar()

    if not pid:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND, detail='not found')

    process = psutil.Process(pid=pid)

    with process.oneshot():
        return dict(
            pid=process.pid,
            name=process.name(),
            username=process.username(),
            status=process.status(),
            cmdline=process.cmdline(),
            create_time=process.create_time(),
            environ=process.environ()
        )


@process_router.get(
    '/stats/{git-user}/{repo-name}',
    response_model=models.ProcessStatsResponse
)
async def getStats(git_user: str, repo_name: str):
    r"""
    get current stats about a process
    """
    repo = f"{git_user}/{repo_name}"
    with database.createSession() as session:
        pid = session.query(dbm.GithubRepository.pid).filter(dbm.GithubRepository.repository == repo).scalar()

    if not pid:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND, detail='not found')

    process = psutil.Process(pid)
    with process.oneshot():
        return dict(
            cpu=process.cpu_percent(),
            memory=process.memory_percent(),
            threads=process.num_threads(),
            # io_counters=process.io_counters()
        )


@process_router.post(
    '/start/{git-user}/{repo-name}',
    response_model=models.StartProcessResponse
)
async def startProcess(git_user: str, repo_name: str):
    await funcStartProcess(f"{git_user}/{repo_name}")


@process_router.post(
    '/stop/{git-user}/{repo-name}',
    response_model=models.StopProcessResponse
)
async def stopProcess(git_user: str, repo_name: str):
    await funcStartProcess(f"{git_user}/{repo_name}")


@process_router.post(
    '/restart/{git-user}/{repo-name}',
    response_model=models.RestartProcessResponse
)
async def restartProcess(git_user: str, repo_name: str):
    repo = f"{git_user}/{repo_name}"
    await funcStopProcess(repo)
    await funcStartProcess(repo)


async def funcStartProcess(repo: str):
    session = database.createSession()
    with session:
        repository = session.query(dbm.GithubRepository).filter(dbm.GithubRepository.repository == repo).first()

    pid = processes.startProcess(repository)

    with session:
        session.query().filter(dbm.GithubRepository.repository == repo).update({'pid': pid})


async def funcStopProcess(repo: str):
    with database.createSession() as session:
        pid = session.query(dbm.GithubRepository.pid).filter(dbm.GithubRepository.repository == repo).scalar()

    processes.stopProcess(pid=pid)


api.include_router(process_router)
