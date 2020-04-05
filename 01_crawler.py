#!/usr/bin/python
#tested on python 2.7
import os 		#to get the URL 
import urllib2  #for parsing html 
from bs4 import BeautifulSoup
import re
import os.path, time	#for reading timestamp

# saludo
print ('\nBienvenidos al final de los tiempos!')

#gets html of the website - ministerio de salud colombia
page_source = '<html><head><title>\nPANDEMONIUM\nusing test html\n</title></head><a href="https://www.minsalud.gov.co/Ministerio/Institucional/Procesos%20y%20procedimientos/GIPS05.pdf"></a><a href="link2"></a><a href="link3"></a></html>'

##response = urllib2.urlopen("https://d2jsqrio60m94k.cloudfront.net/")
##page_source = response.read()

#parsing html
soup = BeautifulSoup(page_source, 'html.parser')

#gets title
print(soup.title.string)

#extracts pdf links to a list
results=[]
for link in soup.findAll('a', attrs={'href': re.compile(".pdf")}):  #<a href="https://www.minsalud.gov.co/Ministerio/Institucional/Procesos%20y%20procedimientos/GIPS05.pdf"></a>
	results.append(link.get('href'));								#https://www.minsalud.gov.co/Ministerio/Institucional/Procesos%20y%20procedimientos/GIPS05.pdf
#	print(link.get('href'))											

for x in results:
	print x
	
	#os.system("wget" link.get('href'))
	
	
	
#	 filePath = 'https://www.minsalud.gov.co/RID/asif13-poblacion-etnica-covid-19-t.pdf'
	
	
# Get file's Last modification time stamp only in terms of seconds since epoch 
#modTimesinceEpoc = os.path.getmtime(filePath)
#modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))

#print("Last Modified Time : ", modTimesinceEpoc )
 

 
#print("Last Modified Time : ", modificationTime )
	
	
	
	



	#filters documents
#pdfs=$()        



