def mul(a, b):                                                             
      if b == 0:                                                              
         return 0                                                             
      pro = mul(a, b-1)                                                     
      value = a+ pro                                                         
      return value


a = 12
b = 34
mul(a, b)
