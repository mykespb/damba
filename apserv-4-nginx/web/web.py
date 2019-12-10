#!/usr/bin/env python
# main runner of damba web
# ver. 3.3. run 2019-12-10
# Mikhail Kolodin

version = '3.3'

params = {}
params['version'] = version
params['web_mode'] = "WSGI"
params['web_driver'] = "hypercorn"

import datetime
import ulid
import redis

from tools import *

from bottle import get, post, route, run, debug, app, template, Bottle, static_file

app = Bottle()

app.config["autojson"] = True

dt = datetime.datetime.now()
dtstr = str(dt)
print ("%s damba engine. starting at %s\n" % (params['web_mode'], dtstr,))

#print ("connect to redis: ", end="")
myredis = None
try:
#    myredis = redis.Redis()
    myredis = redis.Redis(host="db", port=6379, db=0, decode_responses=True)
    params['redis_status'] = "on"
#    print ("connected")
except:
#    print ("cannot connect")
    params['redis_status'] = "off"

tpl = """<!DOCTYPE html><html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<p>This is {{web_mode}} Damba Web ver.{{version}}.</p>
<p>Redis is {{redis_status}}.</p>
<p>Nginx powered.</p>
</body>
</html>
"""


# --------------- decorators

def redis_dec(func):
    """ deco for redis db calls"""

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

    return template (tpl, **params)
#    return "<tt>The nice hello from engine ver.%s at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (
#        version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

# --------------- info

@app.get('/info')
def info():
    """ info req """

    return {"version": version, "datetime_utc": dtstr}

# --------------- putredis
#REDO

@redis_dec
@app.get('/putredis')
def putredis():
    """ test req to set redis value """

    myredis.set("foo", "bar")
    myredis.set("name", "Василий")
    return "set foo=bar, name=Василий"
    
# --------------- getredis
#REDO

@redis_dec
@app.get('/getredis')
def getredis():
    """ test req to get redis value """

    foo = myredis.get("foo")
    name = myredis.get("name")
    return "got foo=%s, name=%s" % (str(foo), str(name))

# ---------------- caller

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=80, debug=True, reload=True)
#    app.run (server='gunicorn', host='0.0.0.0', port=80, debug=True, reload=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.
# =======================================================
