#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import enum
import typing as t
import pydantic


class ProcessStatusEnum(enum.Enum):
    STATUS_RUNNING = "running"
    STATUS_SLEEPING = "sleeping"
    STATUS_DISK_SLEEP = "disk-sleep"
    STATUS_STOPPED = "stopped"
    STATUS_TRACING_STOP = "tracing-stop"
    STATUS_ZOMBIE = "zombie"
    STATUS_DEAD = "dead"
    STATUS_WAKE_KILL = "wake-kill"
    STATUS_WAKING = "waking"
    STATUS_IDLE = "idle"  # Linux, macOS, FreeBSD
    STATUS_LOCKED = "locked"  # FreeBSD
    STATUS_WAITING = "waiting"  # FreeBSD
    STATUS_SUSPENDED = "suspended"  # NetBSD
    STATUS_PARKED = "parked"  # Linux


class ProcessInfoResponse(pydantic.BaseModel):
    pid: int
    name: str
    username: str  # maybe remove
    status: ProcessStatusEnum
    cmdline: t.List[str]
    create_time: float
    environ: t.Dict[str, str]


class ProcessStatsResponse(pydantic.BaseModel):
    cpu: float
    memory: float
    threads: int


class StartProcessResponse(pydantic.BaseModel):
    pass


class StopProcessResponse(pydantic.BaseModel):
    pass


class RestartProcessResponse(pydantic.BaseModel):
    pass
