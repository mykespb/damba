#!/usr/bin/env python
# main runner of damba engine
# ver. 1.7. run 2019-11-19

import datetime
import ulid

#import bottle
from bottle import get, put, route, run, debug, app, template, Bottle

app = Bottle()

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

    return "<tt>hello from engine at %s<br />as long %s [len%d] and short %s [len%d]</tt>" % (dtstr, strmyulid, len(strmyulid), bmyulid, len(bmyulid))

# ---------------- caller
if __name__ == '__main__':
    app.run (server='gunicorn', host='0.0.0.0', port=8080, debug=True)

#    app.debug (True)
#    app.run (host='0.0.0.0', port=8080)
#    app.run (host='localhost', port=8080)

# the end.

