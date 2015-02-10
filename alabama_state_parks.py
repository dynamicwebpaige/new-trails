#! /usr/bin/python

from pyquery import PyQuery
# import pygeocoder
import requests

response = requests.get("http://en.wikipedia.org/wiki/List_of_Alabama_state_parks")
doc = PyQuery(response.content)
holder = []
output = [a.text for a in doc("a")]
holder.append(output)
print holder
