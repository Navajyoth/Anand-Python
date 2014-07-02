import math
epsilon = 0.0000001
def square_root(a, x):
    while True:
        print x
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
  
square_root(5.0, 4.0)   
