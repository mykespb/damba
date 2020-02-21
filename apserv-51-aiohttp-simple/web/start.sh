#!/usr/bin/env bash

hypercorn web:app --reload --debug --bind 0.0.0.0:80 --keep-alive 1000 --workers 1
#hypercorn web:app --bind 0.0.0.0:80 --keep-alive 1000 --workers 4

#gunicorn --workers 17 --bind 0.0.0.0:8000 web:app
#    --worker-class=meinheld.gmeinheld.MeinheldWorker \

#python ./web.py 
