def is_disarium(num):
    digits = str(num)
    total = 0 

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    if total == num:
        return True
    else:
        return False
    



number = int(input("Enter a number: "))



if is_disarium(number):
    print(number, "is a Disarium number")
else:
    print(number, "is Not a Disarium number")