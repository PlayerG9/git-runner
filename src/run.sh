#!/usr/bin/env bash

"$(dirname "$0")/../.venv/bin/uvicorn" "app:app" --app-dir "$(dirname "$0")/git-runner" --host "0.0.0.0" --port 42069 "$@"
