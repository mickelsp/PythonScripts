# Test comment

import urllib2		#Import urllib2 to be able to use Python's webpage reading abilities
from BeautifulSoup import BeautifulSoup		#BeautifulSoup parses the html that we will import

page = urllib2.urlopen("http://www.mobot.org/mobot/research/apweb/ordersside.html")		#Define the URL to open
soup = BeautifulSoup(page)		#Pass the imported html to BeautifulSoup to be parsed

#print soup		#Displays the parsed HTML source code
baseurl = 'http://www.mobot.org/mobot/research/apweb/'	#This is the directory in which all the orders appear
keywords = ['latex','Latex']	#These are the terms that will be searched for in each order page

atags = soup.findAll('a')	#Find all address tags (these contain the order names and web addresses)
urls=[]		#Initialize the URL vector which will contain a list of the URLs for all the different orders
haslatex=[]	#Initialize the vector that will contain '1' for pages that contain 'keyword' and '0' otherwise
f = open('order_results.txt','w')	#Open a file to which to write the results of the keyword searches 
for i in range(1,len(atags)): #Loop through address tags to do a bunch of stuff with them
	tempurl = baseurl+str(atags[i].get('href'))		#Extract the URL from each tag and add to the base URL because the site uses relative addresses
	urls.append(tempurl)	#Add the full URL to the urls vector
	
	ordername = str(atags[i].contents)	#Extract the name of the order
	ordername = ordername[3:-2]			#Strip the extra characters from the order name
	
	orderpage = urllib2.urlopen(tempurl)	#Open the URL for the specific order
	ordersoup = str(BeautifulSoup(orderpage))	#Import the entire source code as a Python string
	
	resultvector = []
	for j in range(0,len(keywords)): 	#Go through each keyword and search the webpage for it
		result = keywords[j] in ordersoup	#Search for the keyword in the webpage (get "True" or "False")
		tempresultvector = [keywords[j],result,ordername,tempurl]	#Create a vector containing the keyword, the result, the name of the order, and the URL that was searched
		#print str(tempresultvector)	#Uncomment to see the results spit out individually
		f.write(str(tempresultvector)+'\n')		#Write results to the text file
		
f.close()	#Close the file to further writing
print 'I am done processing'
	