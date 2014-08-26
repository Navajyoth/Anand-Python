def sqr(x):
    return x*x
def map(sqr, k):
    r = []
    for i in range(k):
        t = sqr(i)
        r.append(t)
    print r


map(sqr,5)
      
