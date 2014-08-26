def perm(a):
    if len(a) <= 1:
       yield a
    else:
        for i in perm(a[1:]):
            for k in range(len(a)):
              yield i[:k] + a[0:1] + i[i:]


perm([1, 2, 3])


