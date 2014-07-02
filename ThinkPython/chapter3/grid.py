def a():
    print'+----+----+'
def b():
    print'|    |    |'

def c():
     b()
     b()

def d():
    c()
    c()

def e():
    a()
    d()
    a()
    d()
    

def f():
    e()
    a()

f() 
