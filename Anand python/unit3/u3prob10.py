import urllib
import json
def my(url):                                                                                                                                       
    a =json.load(urllib.urlopen(url))                                                                                                              
    print a    

my("http://httpbin.org/ip")                                     
