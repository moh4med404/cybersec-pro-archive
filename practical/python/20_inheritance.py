"""
Inheritance in Python:

- Child classes inherit attributes and methods from parent classes.
- Child classes can add or override functionality.
"""

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Child class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id

    # New method specific to Student
    def show_id(self):
        print(f"My student ID is {self.student_id}.")

    # Override display method (optional)
    def display(self):
        super().display()  # Call parent display
        print(f"I am a student with ID: {self.student_id}.")

# Create an instance of Student
student1 = Student("Moha", 21, "S12345")

# Call methods
student1.display()
student1.show_id()
