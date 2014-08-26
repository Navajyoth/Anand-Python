def head(s):
    r =[]
    for line in open(s): 
       r.append(line)
    t =r[0:4]
    for i in t:
      print i
head('cat.txt')
    
    

