#!/usr/bin/python

from mako.template import Template
import cgi
import json

data = json.load(open('data.json'))

html = Template(filename='templates/player.html')
print 'Content-Type: text/html'
print

arguments = cgi.FieldStorage()
if 'v' in arguments:
	try:
		index = int(arguments['v'].value)
	except:
		pass
	else:
		vids = data['videos']
		if index >= 0 and index < len(vids):
			print html.render(playlist=vids[index]['playlist'])


