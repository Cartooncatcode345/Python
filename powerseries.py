for num in range(1, 11):
    print("Power series of", num)
    for i in range(1, 11):
        power = num ** i
        print("%d ^ %d = %d" % (num, i, power))
    print()  # blank line between numbers