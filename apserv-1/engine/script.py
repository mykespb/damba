#!/usr/bin/env python

#print ("Hello to all!")

import datetime

import bottle
#from bottle import get, put, route, run, debug, app

app = bottle.app()

dt = datetime.datetime.now()
dtstr = str(dt)

@bottle.route('/')
def index ():
    return f"hello at {dtstr}"

if __name__ == '__main__':
    bottle.debug (True)
    bottle.run (app=app, host='localhost', port=8080)

