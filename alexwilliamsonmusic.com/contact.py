#!/usr/bin/python

from mako.template import Template
from mako.lookup import TemplateLookup
import json

data = json.load(open('data.json'))

lookup = TemplateLookup(directories=['templates'])

html = Template(filename='templates/contact.html', lookup=lookup)
print 'Content-Type: text/html'
print
print html.render(contact=data['contact'])

