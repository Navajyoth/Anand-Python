def flatten_dict(a, r=None):                                                        #if r is None:
    r ={}
    for key,value in a.items():
         if isinstance(vlaue, dict):
             flatten_dict(value, r)
         else:
              r[key]=value
   # print dict(r)


flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}) 

