#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import time
from _thread import start_new_thread
import schedule


class CustomScheduler(schedule.Scheduler):
    def _run_job(self, job: "schedule.Job") -> None:
        logging.debug(f"running job {job.job_func.func.__name__}")
        start_new_thread(job.run, ())


schedule.default_scheduler = CustomScheduler()


@(lambda fn: start_new_thread(fn, ()))
def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(0.01)
