#!/usr/bin/env bash

#hypercorn script-bottle:app --reload --debug --bind 0.0.0.0:8001 --keep-alive 1000 --workers 1
#hypercorn script-quart:app --reload --debug --bind 0.0.0.0:8001 --keep-alive 1000 --workers 1
#hypercorn script-quart:app --bind 0.0.0.0:8001 --keep-alive 1000 --workers 4

#gunicorn --workers 17 --bind 0.0.0.0:8000 script:app
#    --worker-class=meinheld.gmeinheld.MeinheldWorker \

python ./script-aiohttp.py 
