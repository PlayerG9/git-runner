#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import time
from _thread import start_new_thread
import schedule


@(lambda fn: start_new_thread(fn, ()))
def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(0.01)
