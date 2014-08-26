def cumlative_sum(a):
    tot = 0
    re = []
    for i in a:
      tot += i
      re.append(tot)
    print re
cumlative_sum([1, 2, 3, 4])
cumlative_sum([4, 3, 2, 1])
