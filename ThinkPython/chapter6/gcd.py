#gcd => divident = divisor * qotient * remainder 
def gcd(a, b):
    if a > b:
        #remainder = a%b
        if b == 0:
            return a
        else:
            remainder = a%b
            return (b, remainder)
    else:
        print ('Error it is meant only for a > b')
      
         
gcd(8, 6)
    
