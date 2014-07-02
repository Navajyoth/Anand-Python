import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
def valuepi():
    k = 0
    count = 0
    limit = (1 / 1000000000000000)
    import math
    left = (2 * math.sqrt(2)) / 9801          
    while True:
        up =  factorial(4*k) * (1103 + 26390*k)
        down = factorial(k)  ** 4 * 396**(4*k)
        total = left * up / down
        count += total
        if  total < limit:
            break
        k = k + 1
    return 1 / count
print valuepi() 
