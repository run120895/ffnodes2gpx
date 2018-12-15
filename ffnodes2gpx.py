#!/usr/bin/env python

import requests

r = requests.get("http://api.freifunk-dresden.de/freifunk-nodes.json")
data = r.json()
r.close()

content = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n<gpx version="1.1" creator="Torsten Rudolph">\n"""

i = 0
while True:
  try:
    newwpt = """<wpt lat="%s" lon="%s"><name>%s</name><link href="%s"></link></wpt>\n""" % (data['nodes'][i]['position']['lat'], data['nodes'][i]['position']['long'], data['nodes'][i]['id'], data['nodes'][i]['href'])
    content += newwpt
    i = i+1
  except IndexError:
#    print "while end"
    break

content += "</gpx>"

fobj_out = open("ffdd.gpx", "w")
fobj_out.write(content)
fobj_out.close()

