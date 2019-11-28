#!/usr/bin/env bash

hypercorn script-quart:app --reload --debug --bind 0.0.0.0:8001 --keep-alive 1000 --workers 1
#hypercorn script-quart:app --bind 0.0.0.0:8001 --keep-alive 1000 --workers 4