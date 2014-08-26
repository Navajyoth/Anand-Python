def wget(a):
    import urllib
    import os
    #res = urllib.urlopen(a)
    if os.path.basename(a) == '':
        b = open('index.html', 'w')
        b.write(a)
        b.close()
        j =open('index.html') 
        print j.readline()                                          
    else:
        f = open(os.path.basename(a), 'w')
        f.write(a)
        f.close()
        t =open(os.path.basename(a))
        print t.readline()
        #print res.headers
    

#wget("http://www.google.com")
wget("http://docs.python.org/tutorial/interpreter.html")
#wget("http://docs.python.org/tutorial/")
