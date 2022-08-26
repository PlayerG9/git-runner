#!/usr/bin/env bash

SRCDIR=$(dirname "$0")

"$SRCDIR/../.venv/bin/python3" -B -O "SRCDIR/git-runner/main.py"
