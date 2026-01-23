file_read = open('myself.txt','r')
print("File in read Mode -")
print(file_read.read())
file_read.close()

file_write = open('myself.txt','w')
file_write.write(" I am Nameer ")
file_write.write("My favourtie subjects are science and maths")
file_write.write("I am doing python in codingal")
file_write.write("IDk what to write here")
file_write.close()

file_append = open('myself.txt','a')

file_append.write("\n File in append mode ....")
file_append.write("Hi, I am a codingal student,I learn python")
file_append.close()