#!/usr/bin/env bash

hypercorn web:app --reload --debug --bind 0.0.0.0:80 --keep-alive 1000 --workers 1
#hypercorn web:app --bind 0.0.0.0:80 --keep-alive 1000 --workers 4