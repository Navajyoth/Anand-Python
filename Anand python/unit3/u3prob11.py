import zipfile
def zip(foo, file1, file2):
     z=zipfile.ZipFile(foo, 'w')
     z.write(file1)
     z.write(file2)
     z.close()
     z = zipfile.ZipFile(foo)
     z.printdir()
zip('abc.zip','file1.txt', 'file2.txt')


