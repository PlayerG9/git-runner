#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os


def local(*paths) -> str:
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            *paths
        )
    )


__config: dict = None  # noqa


def getConfig(*keys, default=...):
    global __config
    if not __config:
        import json
        with open(local('config.json')) as file:
            __config = json.load(file)

    config = __config

    try:
        for key in keys:
            config = config[key]
    except (KeyError, IndexError) as error:
        if default is ...:
            raise error
        else:
            return default

    return config
