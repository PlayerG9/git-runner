#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import fastapi
import psutil

from .. import api
from .. import auth
from . import models


process_router = fastapi.APIRouter(prefix="/process")


@process_router.get(
    '/info',
    response_model=models.ProcessInfoResponse
)
async def getInfo(pid: int = fastapi.Query(), _: str = auth.auth):
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
    '/stats',
    response_model=models.ProcessStatsResponse
)
async def getStats(pid: int = fastapi.Query(), _: str = auth.auth):
    process = psutil.Process(pid)
    with process.oneshot():
        return dict(
            cpu=process.cpu_percent(),
            memory=process.memory_percent(),
            threads=process.num_threads(),
            # io_counters=process.io_counters()
        )


api.include_router(process_router)
