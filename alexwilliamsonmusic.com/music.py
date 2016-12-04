#!/usr/bin/python

from mako.template import Template
from mako.lookup import TemplateLookup
import json

data = json.load(open('data.json'))

genres = []
for genre in data['music']:
	display_genre = {}
	display_genre['name'] = genre['genre']
	numsongs = len(genre['songs'])
	halfindex = (numsongs+1)/2
	display_genre['songs_left'] = genre['songs'][:halfindex]
	display_genre['songs_right'] = genre['songs'][halfindex:]
	genres.append(display_genre)

lookup = TemplateLookup(directories=['templates'])

html = Template(filename='templates/music.html', lookup=lookup)
print 'Content-Type: text/html'
print
print html.render(genres=genres)

