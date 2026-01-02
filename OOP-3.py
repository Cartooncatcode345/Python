import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Take input from user
radius = float(input("Enter the radius of the circle: "))

# Create object of Circle class
circle = Circle(radius)

# Display results
print("Area of the circle:", round(circle.area(), 2))
print("Perimeter of the circle:", round(circle.perimeter(), 2))
