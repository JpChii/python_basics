# Working with textual data
# Usage of "", '', """""", depends on the data used.

text = "Hello World"

# Calculate length
print(len(text))

# Indexing through characters
print(f"First character: {text[0]}")
print(f"Last character: {text[len(text) - 1]}")
print("In Slicing first index is inclusive and last index is not inclusive")
print("Starting index 0 and end index 5")
print(f"Index from 0 to 5 with slicing text[0:5]: {text[0:5]}")
print(f"Index 0: {text[0]}, Index 1: {text[5]}")

# Datatypes have a lot of useful inbuilt methods
print("-"*10 + "str.lower() and str.upper()" + "-"*10)
print("Convert text to lower case: text.lower()")
print(f"Lower case: {text.lower()}")
print("Convert text to upper case: text.upper()")
print(f"Upper case: {text.upper()}")
print("-"*10 + "str.lower() and str.upper() ends" + "-"*10+"\n")

print("-"*10 + "str.count()" + "-"*10)
print("We can calculate count of a character or a word in a text using text.count('character/word')")
print(f"Count of 'l' in {text}: {text.count('o')}")
print(f"Count of 'World' in {text}: {text.count('World')}")
print(f"count is case sensitive")
print("-"*10 + "str.count()" + "-"*10 + "\n")

print("-"*10 + "str.find()" + "-"*10)
print(f"To get the index of a character or word in a text, use text.index('character/word')")
print(f"Index of 'l' in {text}: {text.index('l')}")
print(f"Index of 'World' in {text}: {text.index('World')}")
print("For a word find returns the starting index of the word")
print(f"If a word is not present in text, find returns -1")
print(f"Index of 'Universe' in {text}: {text.find('Universe')}")
print("-"*10 + "str.find()" + "-"*10 + "\n")

print("-"*10 + "str.replace()" + "-"*10)
print("Replace takes two arguments: text.replace('old', 'new')")
new_text = text.replace("World", "Universe")
print(f"Old text: {text}")
print(f"New text: {new_text}")
print("-"*10 + "str.replace()" + "-"*10 + "\n")

print("For string concatenation, we can use formatted strings or +. But formatted strings are more cleaner code.")

print("To access all methods available on a variable, use dir(variable)")
print(dir(text))

print("To access documentation for all metods of a datatype use help(datatype)")
print(help(str))

print("To get doc for a specific method, use help(variable.method)")
print(help(text.count))