class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# Creating an instance of the Person class
person = Person("Abdul Hakim", 25)

# Accessing the name and age using getter methods
print(person.get_name())  # Output: Abdul Hakim
print(person.get_age())   # Output: 25

# Modifying the name and age using setter methods
person.set_name("Ryan Hakim")
person.set_age(30)

# Accessing the modified name and age using getter methods
print(person.get_name())  # Output: Ryan Hakim
print(person.get_age())   # Output: 30

# The following line will raise an AttributeError
# print(person.__name)
