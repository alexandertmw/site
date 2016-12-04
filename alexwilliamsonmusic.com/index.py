#!/usr/bin/python

from mako.template import Template
from mako.lookup import TemplateLookup
import json

data = json.load(open('data.json'))

mylookup = TemplateLookup(directories=['/test'])

html = Template(filename='templates/home.html', lookup=TemplateLookup(directories=['templates']))
print 'Content-Type: text/html'
print
print html.render( videos=data['videos'] )

