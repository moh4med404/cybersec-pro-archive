"""
Classes and Objects in Python:

- A class is a blueprint for creating objects.
- An object is an instance of a class.
- The __init__ method is the constructor, called automatically when creating an object.
"""

# Define a class named Person
class Person:
    # Constructor (__init__) to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    # Method to display person's info
    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create an object (instance) of Person
person1 = Person("Moha", 25)

# Call the method on the object
person1.display()


# Create another object
person2 = Person("Adam", 30)
person2.display()
