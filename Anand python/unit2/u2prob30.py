def parse_csv(a):
    t = [[line.strip()] for line in open(a)]
    print t


parse_csv('a.csv')
