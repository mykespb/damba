#!/usr/bin/env python
# main runner of damba engine
# ver. 1.6. ok 2019-11-18

import datetime
import ulid

#import bottle
from bottle import get, put, route, run, debug, app, template, Bottle

app = Bottle()

dt = datetime.datetime.now()
dtstr = str(dt)
print ("damba engine. starting at %s\n" % (dtstr,))

@app.get('/')
def index ():
    dt = datetime.datetime.now()
    dtstr = str(dt)
    myulid = ulid.new().str

    return "<tt>hello from engine at %s as %s [len%d]</tt>" % (dtstr, myulid, len(myulid))

if __name__ == '__main__':
    app.run (server='gunicorn', host='0.0.0.0', port=8080, debug=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

