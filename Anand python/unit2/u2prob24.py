def zip(a, b):
    zip = [] 
    for i in range(max(len(a),len(b))):
      t = (a[i],b[i])
      zip.append(t)
    print zip  



#a = [1, 2, 3]
#b = ['a', 'b', 'c']
zip([1, 2, 3], ['a', 'b', 'c'])
zip(['a', 'b', 'c'],['d', 'e', 'f'])
