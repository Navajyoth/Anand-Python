import math
epsilon = 0.0000001
def square_root(a, x):
    print a,
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    print x,
    built(a)
    
   

def built(x):
     t = math.sqrt(x)
     print t,
     print t - x
square_root(3.0, 3.0)   
