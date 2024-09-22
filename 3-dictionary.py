from utils import print_with_new_line

# Dictionary are key value pair
# Key is a unique idenfiier for data, value is the data that key holds

# Creating a dictionary is done with {}

student = {
    "name": "Hari",
    "age": 19,
    "courses": ["Math", "Physics"]
}

print_with_new_line(f"Dictionary: {student}")

# Values in a dict can be str, int, list, or a dict 
# To access values in a dict, we pass the ke to [] or dict.get(key)
# The key can be an int as well

print_with_new_line(f"Access a key called name in dict: {student.get("name")}")
print_with_new_line(f"What happens when a key isn't present in the dict with get: {student.get("phone")}")
print_with_new_line(f"To returna default value when a key is not present use dict.get('key', 'default value'): {student.get('phone', 'Not present')}")
print_with_new_line(f"What happens when a key is not present in dict with ['key']: throws KeyError")

# To add a new value dict["key"] = value
student["phone"] = "123456"
student["location"] = "Madurai"
# To add a key value pair student.add({'key', 'value'})
print_with_new_line(f"Added new key phone, location to dict: {student}")
# To update a key dict['key] = value
student["location"] = "Theni"
print_with_new_line(f"Updated location from Madurai to theni: {student}")
# To update mutliple values, dict.update({'key': 'value', 'key': 'value'})
student.update({
    "name": "Muthmani",
    "location": "Chennai",
    "phone": "2342434"
})

print_with_new_line(f"After updating multiple keys in dict: {student}")

# To delete a key, value from dict, we can use del and pop
del student["age"]
print_with_new_line(f"After deleting age key with del: {student}")
# With pop popped key's value is retuned
location = student.pop("location")
print(f"Popped location: {location}")
print_with_new_line(f"After popping location key with pop: {student}")

# Access only keys dict.keys()
print_with_new_line(f"Keys: {student.keys()}")
# Access only values dict.values()
print_with_new_line(f"Values: {student.values()}")
# Access both keys and values dict.items()
print_with_new_line(f"Keys and values: {student.items()}")

# To loop only keys for key in dict or for key in dict.keys(
print("Keys")
for key in student:
    print(key)
print_with_new_line("")

# To loop only values for value dict.values()
print("Values")
for value in student:
    print(value)
print_with_new_line("")

# To loop both key and value for key, value in dict.items()
print("Keys, Values")
for key, value in student.items():
    print(key, value)
print_with_new_line("")

