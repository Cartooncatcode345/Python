# Simple calculator for two numbers

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")

choice = input("Enter 1, 2, or 3: ")

# Perform calculation
if choice == "1":
    print("Result:", num1 + num2)

elif choice == "2":
    print("Result:", num1 - num2)

elif choice == "3":
    print("Result:", num1 * num2)

else:
    print("Invalid choice")