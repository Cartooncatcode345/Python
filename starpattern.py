print("Star pattern\n")
n=int(input("Enter Rows="))
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print('\n')


print("Interted star pattern")
for i in range(6,1,-1):
    for j in range(i,1,-1):
        print("*",end=" ")
    print('\n')
