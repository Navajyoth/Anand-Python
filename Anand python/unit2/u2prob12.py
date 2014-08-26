def group(a, b):
     k=len(a)
     m=[]
     while len(a)>0:
       g=[]
       n=0
       for each in a:
          if n>=b:
            break
          g.append(each)
          n+=1
       m.append(g)
       a=a[b:k]
     print m

group([1, 2, 3, 4, 5, 6, 7, 8, 9],4 )
group([1, 2, 3, 4, 5, 6, 7, 8, 9],3)

