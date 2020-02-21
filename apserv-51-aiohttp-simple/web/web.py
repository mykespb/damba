#!/usr/bin/env python
# main runner of simple damba web
# ver. 5.1.1. run 2020-02-21
# Mikhail Kolodin

version = '5.1.1'

params = {}
params['version'] = version
params['web_mode'] = "ASGI"
params['web_driver'] = "aiohttp"

import datetime
import ulid
import aiohttp
import asyncio
from aiohttp import web

from tools import *

dt = datetime.datetime.now()
dtstr = str(dt)
print ("%s damba engine. starting at %s\n" % (params['web_mode'], dtstr,))

tpl = """<!DOCTYPE html><html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<p>This is {{web_mode}} Damba Web ver.{{version}}.</p>
</body>
</html>
"""

# --------------- index

async def info (request):
    """ info req """

    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)
    
    text = tpl % (
        version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

    return web.Response(text=text)


async def index (request):
    """ index req """

    # return web.FileResponse ("./index.html")
    return web.Response (text="HELLO")

# ---------------- caller

#loop = asyncio.get_event_loop()

app = web.Application()

app.add_routes ([
    web.get ('/info', info),
    web.get ('/', index)
    ])

if __name__ == '__main__':
    web.run_app (app)
    
# the end.
# =======================================================
