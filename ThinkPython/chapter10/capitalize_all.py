def capitalize_all(a):
      res = []
      list =[]
      for i in a:
         if type(i) != str:
            for s in i:
               res.append(s.capitalize())
         else:
            list.append(i)
      list.append(res)
      print list
capitalize_all(['a', 'b', 'c', ['d', 'e']])
#capitalize_all([['d', 'e', 'f'], 'f', 'g'])

