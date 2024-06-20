class Circle:
    def __init__(self, radius):
        self.radius = radius
 
    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        return area
 
# Creating an instance of Circle
circle_instance = Circle(5)
 
# Calling the calculate_area method
print("Area of the circle:", circle_instance.calculate_area())