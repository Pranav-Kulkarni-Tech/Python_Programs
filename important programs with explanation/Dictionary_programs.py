# 1. Creating and Initializing Dictionaries

# Empty Dictionary
my_dict = {}
print(my_dict)  # Output: {}

# Dictionary with Key-Value Pairs
fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
print(fruits)  # Output: {'apple': 'red', 'banana': 'yellow', 'orange': 'orange'}

# Using fromkeys() for Default Values
colors = dict.fromkeys(["red", "green", "blue"], "primary")
print(colors)  # Output: {'red': 'primary', 'green': 'primary', 'blue': 'primary'}


# 2. Accessing and Modifying Elements

# Accessing a Value by Key
fruit_color = fruits["apple"]
print(fruit_color)  # Output: red

# Modifying a Value
fruits["banana"] = "pale yellow"
print(fruits)  # Output: {'apple': 'red', 'banana': 'pale yellow', 'orange': 'orange'}

# Adding a New Key-Value Pair
fruits["mango"] = "yellow-orange"
print(fruits)  # Output: {'apple': 'red', 'banana': 'pale yellow', 'orange': 'orange', 'mango': 'yellow-orange'}

# Removing an Element with pop()
removed_fruit = fruits.pop("orange")
print(fruits)  # Output: {'apple': 'red', 'banana': 'pale yellow', 'mango': 'yellow-orange'}


# 3. Iterating through Dictionaries

# Looping through Keys
for fruit in fruits.keys():
    print(fruit)  # Output: apple, banana, mango

# Looping through Values
for color in fruits.values():
    print(color)  # Output: red, pale yellow, yellow-orange

# Looping through Key-Value Pairs (Items)
for item in fruits.items():
    print(item)  # Output: ('apple', 'red'), ('banana', 'pale yellow'), ('mango', 'yellow-orange')


# 4. Using Additional Functions

# Checking if a Key Exists
if "mango" in fruits:
    print("Mango is in the dictionary")
else:
    print("Mango is not in the dictionary")

# Copying a Dictionary
fruit_copy = fruits.copy()
print(fruit_copy)  # Output: {'apple': 'red', 'banana': 'pale yellow', 'mango': 'yellow-orange'}


# Getting a Default Value (using get())
default_color = fruits.get("grape", "purple")  # Returns "purple" as "grape" doesn't exist
print(default_color)  # Output: purple

# Updating a Dictionary with Another Dictionary (using update())
new_fruits = {"kiwi": "green"}
fruits.update(new_fruits)
print(fruits)  # Output: {'apple': 'red', 'banana': 'pale yellow', 'mango': 'yellow-orange', 'kiwi': 'green'}

# Finding the Length (Number of Key-Value Pairs)
num_fruits = len(fruits)
print(num_fruits)  # Output: 4

# Removing the Last Inserted Element (using popitem())
last_added = fruits.popitem()
print(fruits)  # Output: {'apple': 'red', 'banana': 'pale yellow', 'mango': 'yellow-orange'}

# Clearing All Elements (using clear())
fruits.clear()
print(fruits)  # Output: {}
