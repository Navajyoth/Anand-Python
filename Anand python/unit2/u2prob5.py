def pro(c):
    i = 1
    for k in c:
      i *= k
    print i
def fact(a):
    b = range(a+1)
    t =b[1:] 
    pro(t)


fact(5)
