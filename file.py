file = open('document.txt','r')
print(file.read())
file.close()

file = open('document.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()


file = open('document.txt','r')


print(file.readline())
print(file.readline())
print(file.readline())

file.close()