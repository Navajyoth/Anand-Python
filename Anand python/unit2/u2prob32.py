import sys
def mutate(x):
	a=[]
	b=[]
	c=[]
	d=[]
	z=[]
	e=len(x)
	y=['a','b','c','d','e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	f=len(y)
	[a.append(x[0:i]+x[i+1:e]) for i in range(e)]#delete
	[b.append(x[0:i]+y[j]+x[i:e]) for i in range(e+1) for j in range(f)]#insert
	[c.append(x[0:i]+y[j]+x[i+1:e]) for i in range(e) for j in range(f)]#replace
	[d.append(x[0:i]+x[i+1]+x[i]+x[i+2:e]) for i in range(e-1)]#swapping
	z=a+b+c+d
	#print z
	return z

words=mutate('hello')
print 'helo' in words#delete
print 'helblo' in words#insert
print 'cello' in words#replace
print 'hlelo' in words#swapping
