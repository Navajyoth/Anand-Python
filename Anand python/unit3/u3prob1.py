def printdir(dir):
    import os
    filenames = os.listdir(dir)
    for filename in filenames:
        #print filename
        print os.path.join(dir, filename)
        #print os.path.abspath(os.path.join(dir, filename))  

printdir("Downloads")
