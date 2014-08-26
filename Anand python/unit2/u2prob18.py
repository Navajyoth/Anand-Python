def reverselines(s):
    for i in (open(s).readlines()):
        k = reversed(i)
        k = ''.join(reversed(i)) 
        print k

reverselines('cat.txt')

