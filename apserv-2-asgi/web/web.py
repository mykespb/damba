#!/usr/bin/env python
# main runner of damba web
# ver. 2.4. run 2019-11-27
# Mikhail Kolodin

version = '2.4'

params = {}
params['version'] = version
params['web_mode'] = "ASGI"
params['web_driver'] = "hypercorn"

import datetime
import ulid
import redis
import jinja2

from tools import *

from quart import Quart, render_template_string
#, jsonify

app = Quart(__name__)

dt = datetime.datetime.now()
dtstr = str(dt)
print ("%s damba engine with %s. starting at %s\n" % (
    params['web_mode'], 
    params['web_driver'], 
    dtstr,))

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
</body>
</html>
"""

# --------------- bazed ULID

def bazed_ulid(n):
    baza = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bl = len(baza)
    res = ''
    if n == 0:
        return '0'
    while n:
        r = n % bl
        n //= bl
        res = baza[r] + res
    return res

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

@app.route('/')
async def index ():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)

    return await render_template_string(tpl, **params)

# --------------- info

@app.route('/info')
async def info():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    return await render_template_string (f"<tt>{params=}, {dtstr=}</tt>")

# --------------- putredis

@redis_dec
@app.route('/putredis')
async def putredis():
    myredis.set("foo", "bar")
    myredis.set("name", "Василий")
    return await render_template_string (f"set foo=name, name=Василий")
    
# --------------- getredis

@redis_dec
@app.route('/getredis')
async def getredis():
    foo = myredis.get("foo")
    name = myredis.get("name")
    return await render_template_string ("got foo=%s, name=%s" % (str(foo), str(name)))

# ---------------- caller

if __name__ == '__main__':
    app.run (server=params["web_driver"], 
        host='0.0.0.0', port=80, debug=True, reload=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.
# =======================================================
