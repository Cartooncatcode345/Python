# 1. A list with values
fruits = ["apple", "banana", "mango", "orange"]
print("Fruit list:", fruits)

# 2. Dictionary where user adds keys
user_data = {}

how_many = int(input("How many entries do you want to add? "))

for i in range(how_many):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_data[key] = value

print("User dictionary:", user_data)