# Python Object-Oriented Programming
# Classes are nice way of packing methods and attributes for reusabality and code structure
# Classes are blueprints and objects are instances of a class
# We'll create an employee class for an organization
# Methods inside the class recieve the instance as first argument - self
# self.attributes are instance attributes

class Employee:

    # self is the instance of the class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # Define a method to get fullname
    def fullname(self):
        return f"{self.first} {self.last}"

# Creating instances
emp1 = Employee(first="Jp", last="Chi", pay=5000)
emp2 = Employee(first="Test", last="User", pay=6000)
# During this call __init__ method get's called and parameters are passes and set in instance

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())

# The above class performs code reusabality with fullname, instead of creating a formmated string for each employee
# outside class definition, we can just call fullname()
# The self.attributes inside init are instance variables
# If we miss to pass self to fullname(self) in class definition, when we call instance.fullname(), we'll get an error that 1 parameter
# is passed but fullname() doesn't require parameters. This happens because on instance.fullname() call instance get's
# passes as first parameter to the method.
# We can do instance.method() with class as well. But with class we've to pass the instance as th class requires what
# instance is in use. Class.method(instance)