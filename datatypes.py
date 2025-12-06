name = "penguin"
age = 15
is_student = True 
weight = 38.5

print("Name: ", name)
print("Type of name", type(name))

print("Age: ", age)
print("Type of age", type(age))

print("is_student:", is_student)
print("Type of is_student ", type(is_student))

print("Weight: ", weight)
print("Type of weight ", type(weight))

print("After type casting:")

age = str(age)
print("type of age", type(age))

weight = int(weight)
print("Type of weight: ", type(weight))