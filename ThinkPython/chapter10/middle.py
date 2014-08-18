def middle(list):
       del list[0]
       del list[len(list)-1]
       print list

middle([1, 2, 3, 4])
#middle(['a', 'b', 'c', 'd', 'e'])
