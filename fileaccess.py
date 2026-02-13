new_file = open('filer.txt','x')
new_file.close()


import os
print("Checking if my_file exists or not....")
if os.path.exists("filer.txt"):
    os.remove("filer.txt")
else:
    print("The file does not exist")




my_file = open("filer.txt","w")
my_file.write("Hi I am a penguin")
my_file.close()


os.remove('filer.txt')