# Example tuple for demonstration
sample_tuple = (1, 2, 3, 4, 5, 2, 3, 2)

# 1. count() - Counts the occurrences of a specified element in the tuple
count_of_twos = sample_tuple.count(2)
print("1. count(2):", count_of_twos)

# 2. index() - Finds the first occurrence of a specified element in the tuple
index_of_three = sample_tuple.index(3)
print("2. index(3):", index_of_three)

# Additional tuple operations

# 3. Accessing elements by index
first_element = sample_tuple[0]
print("3. First element:", first_element)

# 4. Slicing a tuple
slice_of_tuple = sample_tuple[1:4]
print("4. Slicing (1:4):", slice_of_tuple)

# 5. Iterating through a tuple
print("5. Iterating through tuple:")
for element in sample_tuple:
    print(element, end=" ")
print()

# 6. Checking for existence of an element in a tuple
exists = 3 in sample_tuple
print("6. Existence of 3 in tuple:", exists)

# 7. Concatenating tuples
another_tuple = (6, 7, 8)
concatenated_tuple = sample_tuple + another_tuple
print("7. Concatenated tuple:", concatenated_tuple)

# 8. Multiplying tuples
multiplied_tuple = sample_tuple * 2
print("8. Multiplied tuple:", multiplied_tuple)

# 9. Finding the length of a tuple
length_of_tuple = len(sample_tuple)
print("9. Length of tuple:", length_of_tuple)

# 10. Unpacking tuples
a, b, c, d, e, f, g, h = sample_tuple
print("10. Unpacked tuple elements:", a, b, c, d, e, f, g, h)

# 11. Converting a list to a tuple
list_to_convert = [9, 10, 11]
converted_tuple = tuple(list_to_convert)
print("11. Converted tuple from list:", converted_tuple)

# 12. Converting a tuple to a list
tuple_to_convert = (12, 13, 14)
converted_list = list(tuple_to_convert)
print("12. Converted list from tuple:", converted_list)

# 13. Using a tuple as a dictionary key (tuples are hashable)
tuple_as_key = {(1, 2): "point1", (3, 4): "point2"}
print("13. Tuple as dictionary key:", tuple_as_key)

# 14. Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("14. Nested tuple:", nested_tuple)

# 15. Creating a single-element tuple (requires a comma)
single_element_tuple = (42,)
print("15. Single-element tuple:", single_element_tuple)

# 16. Creating an empty tuple
empty_tuple = ()
print("16. Empty tuple:", empty_tuple)
