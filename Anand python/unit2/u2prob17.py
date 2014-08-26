def reverse(s):
    for i in reversed(open(s).readlines()):
        print i.strip()

reverse('cat.txt')

