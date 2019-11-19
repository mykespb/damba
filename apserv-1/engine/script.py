#!/usr/bin/env python
# main runner of damba engine
# ver. 1.10. run 2019-11-19
# Mikhail Kolodin

import datetime
import ulid

#import bottle
from bottle import get, put, route, run, debug, app, template, Bottle

version = '1.10'

app = Bottle()

app.config["autojson"] = True

dt = datetime.datetime.now()
dtstr = str(dt)
print ("damba engine. starting at %s\n" % (dtstr,))


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


# --------------- web service
@app.get('/')
def index ():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new()
    strmyulid = myulid.str
    intmyulid = myulid.int
    bmyulid = bazed_ulid(intmyulid)

    return "<tt>hello from engine ver.%s at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (
        version, dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

@app.get('/info')
def info():
    return {"version": version, "datetime": dtstr}


# ---------------- caller
if __name__ == '__main__':
    app.run (server='gunicorn', host='0.0.0.0', port=8080, debug=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.
