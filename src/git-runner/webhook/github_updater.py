#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import logging
import requests
import schedule


@schedule.every().minute.do
def updateGithubWebhooks():
    logging.info("Update github-webhooks")
