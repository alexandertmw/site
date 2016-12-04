#!/usr/bin/python

from mako.template import Template
from mako.lookup import TemplateLookup
import json

data = json.load(open('data.json'))

lookup = TemplateLookup(directories=['templates'])

html = Template(filename='templates/about.html', lookup=lookup)
print 'Content-Type: text/html\n\n'
print html.render(about=data['about'])

