#!/usr/bin/env python
# main runner of damba web
# ver. 2.6. run 2019-11-28
# Mikhail Kolodin

version = '2.6'

params = {}
params['version'] = version
params['python_engine'] = "quart"
params['web_mode'] = "ASGI"
params['web_driver'] = "hypercorn"

import datetime
import ulid
import aioredis
import redis
import jinja2

from tools import *

from quart import Quart, render_template_string, render_template

app = Quart(__name__)

dt = datetime.datetime.now()
dtstr = str(dt)
params["dt"] = dtstr

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
    params["dt_now"] = dtstr

    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)
    params["ulid"] = bmyulid

    return await render_template("web-main.html", **params)

# --------------- info

@app.route('/info')
async def info():
    dt = datetime.datetime.now()
    dtstr = str(dt)

    return await render_template_string (f"<tt>aha! {params=}, {dtstr=}</tt>")

# --------------- newmess

@redis_dec
@app.route('/newmessref', methods=['GET', 'POST'])
async def newmessref():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    params["dt_now"] = dtstr

    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)
    params["ulid"] = bmyulid

    myredis.set("newmess", bmyulid)

    return await render_template("web-main.html", **params)

@redis_dec
@app.route('/newmessform', methods=['POST'])
async def newmessform():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    params["dt_now"] = dtstr

    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)
    params["ulid"] = bmyulid

    myredis.set("newmess", bmyulid)

    return await render_template("web-main.html", **params)

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
