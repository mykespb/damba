#!/usr/bin/env python

import datetime

#import bottle
from bottle import get, put, route, run, debug, app

app = bottle.app()

dt = datetime.datetime.now()
dtstr = str(dt)
print ("damba. starting at %s\n" % (dtstr, ))

@app.get('/')
def index ():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    return "hello at %s" % (dtstr,)

if __name__ == '__main__':
    app.debug (True)
    app.run (host='localhost', port=8080)

