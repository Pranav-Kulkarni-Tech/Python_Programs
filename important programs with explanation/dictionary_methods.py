# Example dictionary for demonstration
sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "profession": "Engineer"
}

# 1. clear() - Removes all elements from the dictionary
cleared_dict = sample_dict.copy()
cleared_dict.clear()
print("1. clear():", cleared_dict)

# 2. copy() - Returns a shallow copy of the dictionary
copied_dict = sample_dict.copy()
print("2. copy():", copied_dict)

# 3. fromkeys() - Creates a new dictionary from a sequence of keys with a specified value
keys = ["name", "age", "city"]
default_value = "unknown"
new_dict = dict.fromkeys(keys, default_value)
print("3. fromkeys(keys, default_value):", new_dict)

# 4. get() - Returns the value for a specified key if the key is in the dictionary
age = sample_dict.get("age")
print("4. get('age'):", age)

# 5. items() - Returns a new view of the dictionary's items (key, value pairs)
items = sample_dict.items()
print("5. items():", items)

# 6. keys() - Returns a new view of the dictionary's keys
keys_view = sample_dict.keys()
print("6. keys():", keys_view)

# 7. pop() - Removes the specified key and returns the corresponding value
popped_value = sample_dict.pop("profession")
print("7. pop('profession'):", popped_value)
print("After pop:", sample_dict)

# 8. popitem() - Removes and returns an arbitrary (key, value) pair from the dictionary
sample_dict["profession"] = "Engineer"  # Adding back the key for demonstration
popped_item = sample_dict.popitem()
print("8. popitem():", popped_item)
print("After popitem:", sample_dict)

# 9. setdefault() - Returns the value of a specified key. If the key does not exist, inserts the key with a specified value
default_value = sample_dict.setdefault("country", "USA")
print("9. setdefault('country', 'USA'):", default_value)
print("After setdefault:", sample_dict)

# 10. update() - Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs
sample_dict.update({"city": "Los Angeles", "phone": "123-456-7890"})
print("10. update({'city': 'Los Angeles', 'phone': '123-456-7890'}):", sample_dict)

# 11. values() - Returns a new view of the dictionary's values
values_view = sample_dict.values()
print("11. values():", values_view)

# Additional dictionary operations

# 12. Accessing elements by key
name = sample_dict["name"]
print("12. Accessing 'name':", name)

# 13. Adding a new key-value pair
sample_dict["email"] = "alice@example.com"
print("13. After adding 'email':", sample_dict)

# 14. Checking if a key exists in the dictionary
is_key_present = "age" in sample_dict
print("14. 'age' in sample_dict:", is_key_present)

# 15. Iterating through a dictionary (keys, values, and items)
print("15. Iterating through dictionary keys:")
for key in sample_dict.keys():
    print(key)

print("15. Iterating through dictionary values:")
for value in sample_dict.values():
    print(value)

print("15. Iterating through dictionary items:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")

# 16. Dictionary comprehension
squared_numbers = {x: x*x for x in range(1, 6)}
print("16. Dictionary comprehension (squared numbers):", squared_numbers)

# 17. Merging dictionaries using the | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2
print("17. Merging dictionaries using |:", merged_dict)

# 18. Getting a value with a default if the key is not present
default_age = sample_dict.get("age", "Not specified")
print("18. get('age', 'Not specified'):", default_age)

# 19. Deleting a key-value pair using del
del sample_dict["phone"]
print("19. After del sample_dict['phone']:", sample_dict)
