#! /usr/bin/python

from pyquery import PyQuery
import pygeocoder
import requests

state_parks = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware']
state_parks2 = [ 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas'] 
state_parks3 = ['Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi']
state_parks4 = [ 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New_Hampshire', 'New_Jersey', 'New_Mexico', 'New_York']
state_parks5 = [ 'North_Carolina', 'North_Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South_Carolina']
state_parks6 = [ 'South_Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington']
state_parks7 = [ 'West Virginia', 'Wisconsin', 'Wyoming']

holder = []
holder2 = []
holder3 = []
holder4 = []
holder5 = []
holder6 = []
holder7 = []

for park in state_parks:
	response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
	doc = PyQuery(response.content)
	output = [a.text for a in doc("a")]
	holder.append(output)

print holder

for park in state_parks2:
        response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
        doc = PyQuery(response.content)
        output = [a.text for a in doc("a")]
        holder2.append(output)

print holder2

for park in state_parks3:
        response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
        doc = PyQuery(response.content)
        output = [a.text for a in doc("a")]
        holder3.append(output)

print holder3

for park in state_parks4:
        response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
        doc = PyQuery(response.content)
        output = [a.text for a in doc("a")]
        holder4.append(output)

print holder4

for park in state_parks5:
        response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
        doc = PyQuery(response.content)
        output = [a.text for a in doc("a")]
        holder5.append(output)

print holder5

for park in state_parks6:
        response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
        doc = PyQuery(response.content)
        output = [a.text for a in doc("a")]
        holder6.append(output)

print holder6

for park in state_parks7:
        response = requests.get("http://en.wikipedia.org/wiki/List_of_" + park + "_state_parks")
        doc = PyQuery(response.content)
        output = [a.text for a in doc("a")]
        holder7.append(output)

print holder7



