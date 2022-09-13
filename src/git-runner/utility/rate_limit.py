#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import asyncio
import logging

import fastapi


def rate_limit(times: int, per: int, unit='seconds'):
    call_state = {}
    delay = __unit2seconds(per, unit)

    async def wrapper(request: fastapi.Request, tasks: fastapi.BackgroundTasks):
        # key = f"{request.client.host}:{request.scope['path']}"  # this is a more globally approach
        key = request.client.host
        if call_state.get(key, 0) >= times:
            raise fastapi.HTTPException(
                status_code=fastapi.status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f'too many requests in the last {per} {unit}'
            )
        await increase(key)
        # don't add directly, because fastapi waits for all background-tasks to complete what is no
        # necessary in this case
        tasks.add_task(reduce_later, key)

    async def increase(key: str):
        if key not in call_state:
            call_state[key] = 1
        else:
            call_state[key] += 1

    async def reduce_later(key: str):
        loop = asyncio.get_event_loop()
        if loop is None or loop.is_closed():
            logging.critical('event-loop is None or closed')
        else:
            loop.call_later(delay, reduce, key)

    async def reduce(key: str):
        if key not in call_state:
            return
        if call_state[key] > 0:
            call_state[key] -= 1
        if call_state[key] <= 0:
            del call_state[key]

    return fastapi.Depends(wrapper)


def __unit2seconds(num: int, unit: str) -> int:
    conv_index = {
        'seconds': 1,
        'minutes': 60,
        'hours': 60*60,
        'days': 60*60*24
    }
    factor = conv_index.get(unit, None)
    if factor is None:
        raise ValueError(f'unknown unit: {unit}')
    return num * factor
