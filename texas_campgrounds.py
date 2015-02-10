#! /usr/bin/python

from lxml import html
import requests

west_tx_parks = requests.get('http://texascampgrounds.com/find-a-park?region=West&state=TX&task=findlocation')
west_tree = html.fromstring(west_tx_parks.text)

north_tx_parks = requests.get('http://texascampgrounds.com/find-a-park?region=North&state=TX&task=findlocation')
north_tree = html.fromstring(north_tx_parks.text)

central_tx_parks = requests.get('http://texascampgrounds.com/find-a-park?region=Central&state=TX&task=findlocation')
central_tree = html.fromstring(central_tx_parks.text)

east_tx_parks = requests.get('http://texascampgrounds.com/find-a-park?region=East&state=TX&task=findlocation')
east_tree = html.fromstring(east_tx_parks.text)

gulf_coast_parks = requests.get('http://texascampgrounds.com/find-a-park?region=North%20Gulf%20Coast&state=TX&task=findlocation')
gulf_tree = html.fromstring(gulf_coast_parks.text)

south_gulf_coast_parks = requests.get('http://texascampgrounds.com/find-a-park?region=South%20Gulf%20Coast&state=TX&task=findlocation')
south_gulf_tree = html.fromstring(south_gulf_coast_parks.text)

south_tx_parks = requests.get('http://texascampgrounds.com/find-a-park?region=South&state=TX&task=findlocation')
south_tree = html.fromstring(south_tx_parks.text)

parkname = west_tree.xpath('/html/body/div/div[3]/center/div/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td/div/div[1]/a/strong')
print parkname[0].tag

