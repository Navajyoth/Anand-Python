def check_fermat(a, b, c, n):                                               
    if n > 2:                                                               
         left = a**n + b**n
         right = c**n                                                        
         left == right                                                      
         print "Holy smokes, Fermat was wrong!"
    else:
         print "That Doesn't work"

