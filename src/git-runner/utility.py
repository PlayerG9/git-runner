#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import os


def local(*paths) -> str:
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            *paths
        )
    )


def getConfig() -> dict:
    import json
    with open(local('config.json')) as file:
        return json.load(file)
