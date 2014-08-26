def cumulative_product(a):
    re = []
    pro = 1
    for i in a:
      pro *= i
      re.append(pro)
    print re



cumulative_product([1, 2, 3, 4])
cumulative_product([4, 3, 2, 1])
