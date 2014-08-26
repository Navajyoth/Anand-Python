def reverse(a):
    list = []
    for i in a:
        t = a[len(a) - i]
        list.append(t)
    print  list     
#k = [1, 2, 3, 4, 5]
#reverse(k)
reverse([1, 2, 3, 4])
