"""
Inheritance
Leveraging existing class methods and attributes and building on top of it without disturbing
the original class

Let's create developer and manager class inheriting Employee class
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

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        return int(self.pay * self.raise_percent)
    
    @classmethod
    def set_raise_method(cls, amount):
        cls.raise_percent = amount 

# Let's see how inheritance works with model resolution order
class Developer(Employee):
    pass

# When we instantiate an object for developer class. It tries to find __init__ method inside Developer class
# Then it checks Employee class, what attributes are available, methods etc are available in 
# model resolution order. To access this info pass class to help()

# print(help(Developer))

# let's perform some simple change and some complex changes to the Developer class
# We want an additional parameter programming language for Developer class.
# To do this we can use __init__ of Employee and add prog_lang parameter.
# Use super().__init__() to call initializaiton of employee class and pass first, last, pay to super init
# with this approach we don't have to repeate the code in Employee init class and keep the code DRY

class Developer(Employee):

    # Developer have a higher raise percentage
    raise_percent = 1.15
    def __init__(self, first, last, pay, prog_lang):
        # Initializes Employee __init__ method, we've avoided attribute creation for first, last, pay
        # This keeps the code DRY
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev1 = Developer(first="Jp", last="Chi", pay=5000, prog_lang="Python")
print(f"Employee raise amount: {Employee.raise_percent}")
print(f"Developer raise amount: {dev1.raise_percent}")
print("Updating Developer raise amount to 1.12")
dev1.set_raise_method(amount=1.12)
print(f"Employee raise amount: {Employee.raise_percent}")
print(f"Developer raise amount: {dev1.raise_percent}")
print("Updating Developer raise amount to 1.12")
print("Employee attribut isn't updated only Developer attribute is updated. This is the advantage of class inheritance.")

# Let's create a manager class and add more functionalities to it. An additonal employees class to hold employees managed by the Manager
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        return self.employees
    
    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        return self.employees
    
    def print_emps(self):
        for emp in self.employees:
            print(f"=>{emp.fullname()}")

# Adding employee
dev2 = Developer(first="Jp", last="Shin", pay=5000, prog_lang="Java")
mgr1 = Manager(first="Hari", last="Karvan", pay=10000)
mgr1.add_emp(dev1)
mgr1.add_emp(dev2)
print(f"Employess with manager:")
mgr1.print_emps()
print("Deleting Jp Shin")
mgr1.remove_emp(dev2)
print(f"Employess with manager after delete:")
mgr1.print_emps()

# There are some useful methods to check if an instance belongs to a particular class or subclass or if an attribute is present in a class or not
print_with_new_line("")
print(f"Is dev1 a instance of Developer class: {isinstance(dev1, Developer)}")
print(f"Is dev1 a instance of Employee class: {isinstance(dev1, Employee)}")
print(f"Is dev1 a instance of Manager class: {isinstance(dev1, Manager)}")
print_with_new_line("")
print(f"Is Developer a subclass of Employee: {issubclass(Developer, Employee)}")
print(f"Is Manager a subclass of Employee: {issubclass(Manager, Employee)}")
print(f"Is Manager a subclass of Developer: {issubclass(Manager, Developer)}")
print(f"Is Developer a subclass of Manager: {issubclass(Developer, Manager)}")
print_with_new_line("")
print("Checking attributes")
print(f"Is raise_amount present in Manager: {hasattr(mgr1, "raise_percent")}")
# Even though raise_percent is not present in Manager explicitly it's inherited from Employee class