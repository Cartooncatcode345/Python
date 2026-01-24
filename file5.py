new_file = open('New_file.txt','x')
new_file.close()


import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")




my_file = open("my_file.txt","w")
my_file.write("Hi I am a penguin")
my_file.close()


os.remove('clone.txt')


#os.rmdir('ah')
