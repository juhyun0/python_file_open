file=open('test.txt','w')
file.write('hello')
file.close()

file=open('test.txt','r')
str=file.read()
print(str)
file.close()
