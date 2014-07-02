def do_n(s, m, n):                                                          
    if n <= 0:                                                             
        return                                                             
    print s, m                                                             
    do_n(s, m, n-1) 
