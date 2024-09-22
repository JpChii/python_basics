# lists in python as name says lists to store a list of values, object etc
# List can be created with []
from utils import print_with_new_line

locations = ["Chennai", "Madurai", "Tricy", "Theni", "Kanchipuram"]
print_with_new_line(f"Locations list: {locations}")

# Accessing lists
# Length of list can be accessed using len
print_with_new_line(f"Number of elements in list: {len(locations)}")

# Lists can be accessed using indexes and slicing
# indexes start from 0 and len_of_list - 1
# access a single element
print_with_new_line(f"Accessing first element: {locations[0]}")
print_with_new_line(f"Accessing second element: {locations[1]}")
# negative -1 to access last element in index, 
# this is much more robust than subracting 1 from length of list and accessing the element. when a list changes all the time
print_with_new_line(f"Accessing last element with -1: {locations[-1]}")
# and so on

# Select multiple elements in lists with slicing
# slicing is performed with :
# start_index:end_index, start_index is inclusive and end_index is exclusive. This is to accomodate for
# length and index difference. length(calculated from 1), index(starts from 0)
# If start or end index is not specified then it's assumed to be from  start or end of list respectiley
print_with_new_line(f"Access first two elements: {locations[0:2]}") # Can also be accessed with locations[:2]
print_with_new_line(f"Access last two elements: {locations[-2:]}")
print_with_new_line(f"Start from second index and print_with_new_line all elements until end: {locations[2:]}")
print_with_new_line(f"All elements: {locations[:]}")

# Modifying lists
# To add an element to the end of a list
print_with_new_line(f"Adding Cheyyar to the list")
locations.append("Cheyyar")
print_with_new_line(locations[:])
# Add elements at a specific position
print_with_new_line(f"Adding element to first index")
locations.insert(0, "Unknown_location")
print_with_new_line(locations[:])
print_with_new_line(f"Joining two lists together")
new_locations = ["Kochi", "Thrissur", "Trivandram"]
# With extend() elements from one list will be added to another list
print_with_new_line(f"New locations list: {new_locations}")
locations.extend(new_locations)
print_with_new_line(f"Joined list: {locations}")
# To remove an element from any position at the list, remove("value in list")
locations.remove("Theni")
print_with_new_line(f"Removing element from anywhere: {locations}")
# To remove an element at the end of list pop(). pop also returns the removed element
pop = locations.pop()
print_with_new_line(f"Element removed with pop: {pop}")
print_with_new_line(f"List after removal of last element")
print_with_new_line(locations)

# Sorting, finding values, looping lists, splitting and joining lists
# To sort a list in place
copied_list = locations.copy()
copied_list.sort()
print_with_new_line(f"Sorted string list: {copied_list}")
# String items are sorted in alphabetical order
# To sort without affecting the original list use sorted(iterable_list)
new_sorted_list = sorted(locations)
print_with_new_line(f"Sorting with keeping the original copy as is: {new_sorted_list}")
print_with_new_line(f"Original list after sort: {locations}")
# To sort a list in reverse 
print_with_new_line(f"Reverse sort: {locations.sort(reverse=True)}")
# A numerical list gets sorted in ascending order
num_list = [4,1,23,5,6]
print_with_new_line(f"Numerical list: {num_list}")
num_list.sort()
print_with_new_line(f"Numerical list sort: {num_list}")
num_list.sort(reverse=True)
print_with_new_line(f"Numerical list sort reverse: {num_list}")
print_with_new_line(f"After in place sort, original list: {num_list}")

# Looping with lists
# To loop through elements in a list we can use for loop
print("Looping with for")
for location in locations:
    print(location)
print_with_new_line("")

# to loop with index we can use enumerate()
print("Enumerate")
for idx, location in enumerate(locations):
    print(f"Index: {idx}, Location: {location}")
print_with_new_line("")

# To loop from specific index we can use enumerate(position_to_start)
print("Enumerate from a specific index")
for idx, location in enumerate(locations, start=3):
    print(f"Index: {idx}, Location: {location}")
print_with_new_line("")

# Joining and splitting
# We can join a list of elements with "deleimieter".join(list)
joined_locations = ",".join(locations)
print_with_new_line(f"Joined locatins with comma as delimiter: {joined_locations}")
print_with_new_line(f"Split joined locations by delimiter: {joined_locations.split(',')}")

# Tuples can't be modified - in programming words immutable
# To create a tuple use (), for unchanging list or object we can use tuples instead of lists
# Tuples doesn't have pop, append etc. But we can perform indexing, looping, joining splitting as in lists
states = ("TN", "KL", "AP", "KA")
print(type(states))
print(f"States: {states}")
print(f"Slicing first two elements: {states[:2]}")
print(f"Joining states: {','.join(states)}")
print_with_new_line("")

# Sets can be created with {}, remove duplicates, unordered
fruits_basket_1 = {"Apple", "Oranges", "Banana", "Pomegranate"}
print(type(fruits_basket_1))
print("Displaying unordered nature of sets")
print(fruits_basket_1)
print(fruits_basket_1)
print(fruits_basket_1)
print("Adding apple again to set")
fruits_basket_1.add("Apple")
# We don't get two Apple because sets remove duplicates
print(fruits_basket_1)

print_with_new_line("")
# Finding commonalites between two sets
fruits_basket_2 = {"Mango", "Oranges", "Lemon"}
print(f"Basket 1: {fruits_basket_1}")
print(f"Basket 2: {fruits_basket_2}")
print(f"Common fruits between two baskets: {fruits_basket_1.intersection(fruits_basket_2)}")
print(f"Fruits in  basket 1 and not in basket 2: {fruits_basket_1.difference(fruits_basket_2)}")
print(f"Fruits in basket 2 not in basket 1: {fruits_basket_2.difference(fruits_basket_1)}")
print(f"Fruits in both baskets: {fruits_basket_1.union(fruits_basket_2)}")