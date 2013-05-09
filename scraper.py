import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.wrh.noaa.gov/twc/monsoon/monsoon.php")
soup = BeautifulSoup(page)

years1 = soup.findAll('font')

# for x in range(49,750):
mystring = years1[749]
print years1[749]

print mystring(1)
# for x in range(0,len(years1)):
# 	mystring = years1[x]
# 	for s in mystring:
# 		print years1[450]

