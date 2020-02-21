#!/usr/bin/env python
# main runner of damba web
# ver. 3.4. run 2020-02-21
# Mikhail Kolodin

version = '4.1'

params = {}
params['version'] = version
params['web_mode'] = "ASGI"
params['web_driver'] = "aiohttp"

import datetime
import ulid
import redis
#~ import aiohttp
import asyncio
from aiohttp import web

from tools import *

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

async def handle(request):
    """ index req """

    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)
    
    text = tpl % (
        version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

#    return template (tpl, **params)
    return web.Response (text=text)
    
#    return "<tt>The nice hello from engine ver.%s at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (
#        version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

# ---------------- caller

app = web.Application()

app.add_route (web.get ('/', handle))

if __name__ == '__main__':
    web.run_app (app)
    
# the end.
# =======================================================
