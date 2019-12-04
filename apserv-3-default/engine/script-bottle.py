#!/usr/bin/env python
# main runner of damba engine
# ver. 3.2 run 2019-12-04
# Mikhail Kolodin

version = '3.2'

params = {}
params['version'] = version
params['python_engine'] = "bottle"
params['web_mode'] = "WSGI"
params['web_driver'] = "python"

import datetime
import ulid
import redis

from tools import *

from bottle import get, post, route, run, debug, app, Bottle

app = Bottle()

app.config["autojson"] = True

dt = datetime.datetime.now()
dtstr = str(dt)
print ("%s damba engine. starting at %s\n" % (params["web_mode"], dtstr,))

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
    """ test req to set redis value """

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
    """ index req """

    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)

    return "<tt>The %s hello from engine %s with ver.%s at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (
        params["web_mode"], params["web_driver"], version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

# --------------- info

@app.get('/info')
def info():
    """ info req """

    dt = datetime.datetime.now()
    dtstr = str(dt)
    return {**params, "dt_now": dtstr}

# --------------- putredis

@redis_dec
@app.get('/putredis')
def putredis():
    """ test req to set redis value """

    myredis.set("foo", "bar")
    myredis.set("name", "Василий")
    return "set foo=bar, name=Василий"
    
# --------------- getredis

@redis_dec
@app.get('/getredis')
def getredis():
    """ test req to get redis value """

    foo = myredis.get("foo")
    name = myredis.get("name")
    return "got foo=%s, name=%s" % (str(foo), str(name))

# ---------------- caller

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=8001, debug=True, reload=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.
# =======================================================
