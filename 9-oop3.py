"""
ClassMethods
* Regular methods takes instance as the first argument
* Class methods takes class itself as first argument
* To create a class methos use @classmethod decorator and pass cls as the first argument
class method works with the class itself and not the instance
* We can use classmethod as alternative constructor as well. Take an example if there's another input format
for employee data as str first-last-pay, instead of parsing this everytime with split and passing it to
the Employee class, we can create a class method split this within and return Employee class object.
* Realtime examples of classmethod as alternative constructors can be seen in datetime module. fromtimestamp is a class method.

StaticMethods
* StaticMethods are methods that doesn't requires instance or class as it's arguement. 
* In other words they don't require any attributes or methods from the class but has a logical connection with the class.
* Example to check if a day is working day or not. It doesn't require first, last, pay, num_of_emps, raise_percent, fullname() etc.
* In this we can create this as a staticmethod
"""

from utils import print_with_new_line
import datetime
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
    
    
    # Class Method, accepts class as the first parameter
    @classmethod
    def set_raise_method(cls, amount):
        cls.raise_percent = amount 

    # Alternative constructor with classmethod
    # We can use classmethod as alternative constructor as well. Take an example if there's another input format
    # for employee data as str first-last-pay, instead of parsing this everytime with split and passing it to
    # the Employee class, we can create a class method split this within and return Employee class object.
    @classmethod
    def fromstring(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day: datetime.date):
        if day.weekday() in [5, 6]:
            return False
        return True

# Creating instances
emp1 = Employee(first="Jp", last="Chi", pay=5000)
emp2 = Employee(first="Test", last="User", pay=6000)

print("Initial raise percent")
print(Employee.raise_percent)
print(emp1.raise_percent)
print(emp2.raise_percent)
print_with_new_line("")
print("Setting raise_amount with class method")
emp1.set_raise_method(1.06)
print(Employee.raise_percent)
print(emp1.raise_percent)
print(emp2.raise_percent)
# even though we're updating the parameter from an instance, we are setting the value to 
# class variable using class method
print_with_new_line("")
print(f"Using alternative constructor with class method for different input fomrat")
emp_str1 = "Jp-chi-5000"
emp_str2 = "Test-User-6000"
print(f"Input strs: {emp_str1},{emp_str1}")
emp1 = Employee.fromstring(emp_str1)
emp2 = Employee.fromstring(emp_str2)
print(f"Email for emp1: {emp1.email}")
print(f"Email for emp2: {emp2.email}")
print_with_new_line("")
print("Using staticmethod")
print(Employee.is_workday(datetime.date(2023, 9, 23)))
print_with_new_line("")