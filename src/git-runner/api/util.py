#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import typing as t
from http import HTTPStatus


__status_text__ = {status.value: (status.phrase, status.description or None) for status in list(HTTPStatus)}
__default_status__ = ('Internal Server Error', 'Server got itself in trouble')


def status2info(code: int) -> t.Tuple[str, t.Optional[str]]:
    return __status_text__.get(code, __default_status__)
