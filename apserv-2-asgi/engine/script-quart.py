#!/usr/bin/env python
# main runner of damba engine
# ver. 2.8. run 2019-12-04
# Mikhail Kolodin

version = '2.8'

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

from quart import Quart, render_template_string, websocket

app = Quart(__name__)

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
    """ deco for redis db calls"""

    def wrapper(*args, **kwargs):
        if myredis:
            func(*args, **kwargs)
        else:
            return "no redis connection"
    return wrapper

# --------------- websockets

# @app.websocket('/ws')
# async def wsproc():
#     while True:
#         info = await websocket.receive()
#         if info and type(info) == str:
#             inforev = info.reverse()
#             await websocket.send(inforev)

# --------------- index

@app.route('/')
async def index ():
    """ info req """

    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)

    return await render_template_string("<tt>The %s hello from engine %s with ver.%s at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (
        params["web_mode"], params["web_driver"], version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid)))

# ---------------- caller

if __name__ == '__main__':
    app.run (server=params["web_driver"],
        host='0.0.0.0', port=8001, debug=True, reload=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.
# =======================================================
