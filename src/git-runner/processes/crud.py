#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os
import typing as t
import subprocess
import psutil
import platform
from database.models import GithubRepository


def startProcess(repository: GithubRepository) -> int:
    # cmdline: t.List[str], env: dict = None
    cmdline = repository.command
    env = repository.environment

    config = {}

    # this is supposed to run only on linux but still
    if platform.platform() == 'Windows':
        config.update(creationFlags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
    else:
        config.update(start_new_session=True)

    process = subprocess.Popen(
        cmdline,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env or {},
        **config
    )

    return process.pid


def stopProcess(pid: int):
    process = psutil.Process(pid=pid)
    if process.ppid() != os.getpid():
        raise PermissionError("not allowed to kill this process")
    process.terminate()
    try:
        process.wait(timeout=1)
    except psutil.TimeoutExpired:
        process.kill()
        try:
            process.wait(timeout=1)
        except psutil.TimeoutExpired:
            pass
    if process.is_running():
        raise psutil.Error("couldn't kill process")
