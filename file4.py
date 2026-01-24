with open ("document.txt","w") as f:
    f.write("Hello world!!!")


f.close()



with open ("document.txt","r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)



file.close()

