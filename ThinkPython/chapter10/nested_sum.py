def nested_sum(a):
    sum1 =0
    sum2 =0
    for i in a:
        if type(i) != int:
            for k in i:
                sum1 += k
        else:
            sum2 += i
    print sum1+sum2


#nested_sum([1, 2, 3,[4, 5, 6]])
nested_sum([1, 2, 3, 4, [1, 2], [1, 2]])    
