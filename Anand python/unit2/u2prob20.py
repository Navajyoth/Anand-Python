def grep(s, i): 
    for line in open(s):
      if i in line:
        print line

grep('cat.txt', 'sure')
