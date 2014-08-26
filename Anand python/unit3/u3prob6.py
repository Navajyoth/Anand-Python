import urllib
import re
def antihtml(url):
    res = urllib.urlopen(url)
    html =res.readlines()
    for each in html:                                                      
         match = re.search('(<)(\w+)(>)', each)                             
         if match:                                                          
             print match.group(2)




antihtml("http://www.w3schools.com/html/html_examples.asp") 
