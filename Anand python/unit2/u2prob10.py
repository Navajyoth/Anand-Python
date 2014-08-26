def unique(a):
      c = []
      for i in a:
          while i not in c:
              c.append(i)
      #return c 
      print c
  
unique([1, 2, 1, 3, 2, 5])    
