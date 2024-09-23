"""
* Class variable remains same for all instance unlike instance variable
* Raise percentage remains same for all employees, we can put such attributes as class variables
* We can access class variables using class.variable or self.variable, why class variables inside instance?
While accessing a variable the class first checks the instance if it's present or not else it'll check
the class for the variable
* instance variables can be viewed under instance.__dict__ and class variables with class.__dict__
* Setting or updating a class variable with class updates it for instances as well
* Setting or updating a class variable within instance doesn't update the class variable. Why because it creates
a new instance variable during update
* This is important because, based on the update to class variable we can get different results for raise of
different employees
* Accessing class variables with self will allow any sub classess to update the variable if required
For example. we've num_of_employees class variable. This doesn't have the need to updated by sub classes.
We can use class.num_of_employees
"""

from utils import print_with_new_line
class Employee:

    # Class variables
    num_of_emps = 0
    raise_percent = 1.05

    def __init__(self, first, last, pay):
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        # Using class variable with class itself, this can't be updated by subclasses. if num_of_emps is updated by an instance it creates a new
        # variable num_of_emps for the instance and updates it
        Employee.num_of_emps += 1

    # Define a method to get fullname
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def raise_amount(self):
        # By accessing raise_percent with self, this allows subclasses to modify this value
        # This allows us to have different raise_percent for different employees
        return int(self.pay * self.raise_percent)
    
# Creating instances
emp1 = Employee(first="Jp", last="Chi", pay=5000)
emp2 = Employee(first="Test", last="User", pay=6000)

print("Initial raise percent")
print(Employee.raise_percent)
# Here class variable is accessible because, instance first check instance attributes and then class attributes
print(emp1.raise_percent)
print(emp2.raise_percent)
print_with_new_line("")
print_with_new_line(f"Instance attributes: {emp1.__dict__}")
print(f"Class attributes: {Employee.__dict__}")
print("Note class vars num_of_emps and raise_percent are not available for instance directly")
print_with_new_line("")
print("Update raise percent to 1.08")
# Setting or updating a class variable with class updates it for instances as well
Employee.raise_percent = 1.08
print(Employee.raise_percent)
print(emp1.raise_percent)
print(emp2.raise_percent)
print_with_new_line("")
print("Update raise percent of emp2 to 1.10")
# Setting or updating a class variable within instance doesn't update the class variable. Why because it creates
# a new instance variable during update
emp2.raise_percent = 1.12
print(Employee.raise_percent)
print(emp1.raise_percent)
print(emp2.raise_percent)
print_with_new_line("")