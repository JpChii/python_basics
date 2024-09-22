# Functions are a way to package of set of instructions
# To define a function and write its functionality later, use pass
from utils import print_with_new_line
# placeholder function
def placeholder():
    pass

print(placeholder())

# Functions are way to keep your code DRY(Don't Repeat Your) code.
# Instead of running a same code multiple times in multiple files across the codebase
# We can define it in a function and call it across the codebase, Ex: print_with_new_line function in utils.py

# What's *args and **kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Math", "Art", name="John", age=22)

# args becomes tuple inside function, kwargs are key value pairs inside function

# to pass positional arguments and key word arguments via list and dict. We can use * and ** to unpack
print_with_new_line("")
print("Function without unpacked arguments")
courses = ["Math", "Art"]
info = {'name': 'John', 'age': 22}
student_info(courses, info)
print_with_new_line("")
print("Function with unpacked arguments")
student_info(*courses, **info)
print_with_new_line("")