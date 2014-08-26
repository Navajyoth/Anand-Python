def extcount(dir):
    import os
    a = os.listdir(dir) 
    v = a.sort(key=lambda f: os.path.splitext(f)[1])
    print a
extcount("Documents")
