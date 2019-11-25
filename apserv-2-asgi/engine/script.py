#!/usr/bin/env python
# main runner of damba engine
# ver. 2.1. run 2019-11-25
# Mikhail Kolodin

version = '2.1'

import datetime
import ulid
import redis

from tools import *

#import bottle
from bottle import get, post, route, run, debug, app, Bottle

app = Bottle()

app.config["autojson"] = True

dt = datetime.datetime.now()
dtstr = str(dt)
print ("ASGI damba engine. starting at %s\n" % (dtstr,))

print ("connect to redis: ", end="")
myredis = None
try:
#    myredis = redis.Redis()
    myredis = redis.Redis(host="db", port=6379, db=0, decode_responses=True)
    print ("connected")
except:
    print ("cannot connect")

# --------------- decorators

def redis_dec(func):
    def wrapper(*args, **kwargs):
        if myredis:
            func(*args, **kwargs)
        else:
            return "no redis connection"
    return wrapper

# --------------- web services

# --------------- index

@app.get('/')
def index ():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)

    return "<tt>The ASGI hello from engine ver.%s at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (
        version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

# --------------- info

@app.get('/info')
def info():
    return {"version": version, "datetime_utc": dtstr}

# --------------- putredis

@redis_dec
@app.get('/putredis')
def putredis():
    myredis.set("foo", "bar")
    myredis.set("name", "Василий")
    return "set foo=bar, name=Василий"
    
# --------------- getredis

@redis_dec
@app.get('/getredis')
def getredis():
    foo = myredis.get("foo")
    name = myredis.get("name")
    return "got foo=%s, name=%s" % (str(foo), str(name))

# ---------------- caller

if __name__ == '__main__':
    app.run (server='gunicorn', host='0.0.0.0', port=8001, debug=True, reload=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.
# =======================================================
