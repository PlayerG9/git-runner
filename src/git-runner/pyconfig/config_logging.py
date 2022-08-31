#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import logging.handlers as loghandler


file_handler = loghandler.RotatingFileHandler(
    filename='git-runner.log',
    maxBytes=1024*1024*10,
    backupCount=5
)


console_handler = logging.StreamHandler()


logging.basicConfig(
    format="{asctime} | {levelname:.3} | {module}-{lineno} | {funcName} | {message}",
    style="{",
    level=logging.DEBUG,
    handlers=[
        file_handler,
        console_handler
    ]
)
