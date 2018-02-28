from urllib.request import urlopen
import json
import numpy
# import requests
# from BeautifulSoup import BeautifulSoup
# import tbapy

response = urlopen('http://pythonforbeginners.com/')
print(response.info())

# html = response.read()
# print html

# soup = BeautifulSoup(html)
# print soup.prettify

# tba = tbapy.TBA('VD5od8PULvq44hVjgZOJUpDHQehGicwjGyEPeXmNpIyyDP6I11qp226eSKLJHjZF')
# fish = tba.team(649, True)
matches = 3
print(matches)
