def lensort(a):
     b = []
     for i in sorted(a, key= lambda a:len(a)):
         b.append(i)
     print b

lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
      
