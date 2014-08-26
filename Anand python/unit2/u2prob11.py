def dups(a):
    c =[]
    b =[]
    for i in a:
       if i not in c:
         c.append(i)
       else:
          b.append(i)
    print b
dups([1, 2, 1, 3, 2, 5])


