def inverdic(a):
     for i, j in a.items():
         del a[i]
         a[j] =i
     print a


#a ={1:'a', 2:'b'}
inverdic({'a':1, 'b':2})
         
