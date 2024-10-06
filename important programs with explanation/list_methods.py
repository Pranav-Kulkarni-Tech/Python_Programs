# Initializing a sample list
sample_list = [1, 2, 3, 4, 5]

# 1. append() - Adds an element to the end of the list
sample_list.append(6)
print("1. append(6):", sample_list)

# 2. extend() - Adds all elements of an iterable (list, tuple, string, etc.) to the end of the list
sample_list.extend([7, 8, 9])
print("2. extend([7, 8, 9]):", sample_list)

# 3. insert() - Inserts an element at a specified position
sample_list.insert(3, 10)  # Insert 10 at index 3
print("3. insert(3, 10):", sample_list)

# 4. remove() - Removes the first occurrence of a specified value
sample_list.remove(10)
print("4. remove(10):", sample_list)

# 5. pop() - Removes and returns the element at the specified position (default is the last element)
popped_element = sample_list.pop()
print("5. pop():", popped_element)
print("After pop():", sample_list)

# 6. clear() - Removes all elements from the list
cleared_list = sample_list.copy()  # Creating a copy to clear
cleared_list.clear()
print("6. clear():", cleared_list)

# 7. index() - Returns the index of the first occurrence of a specified value
index_of_3 = sample_list.index(3)
print("7. index(3):", index_of_3)

# 8. count() - Returns the number of occurrences of a specified value
count_of_3 = sample_list.count(3)
print("8. count(3):", count_of_3)

# 9. sort() - Sorts the list in ascending order (can take optional parameters for reverse sort and a key function)
unsorted_list = [3, 1, 4, 5, 2]
unsorted_list.sort()
print("9. sort():", unsorted_list)

# 10. reverse() - Reverses the elements of the list in place
unsorted_list.reverse()
print("10. reverse():", unsorted_list)

# 11. copy() - Returns a shallow copy of the list
copied_list = sample_list.copy()
print("11. copy():", copied_list)

# 12. len() - Returns the length of the list
length = len(sample_list)
print("12. len():", length)

# 13. max() - Returns the maximum value in the list
max_value = max(sample_list)
print("13. max():", max_value)

# 14. min() - Returns the minimum value in the list
min_value = min(sample_list)
print("14. min():", min_value)

# 15. sum() - Returns the sum of all elements in the list
total_sum = sum(sample_list)
print("15. sum():", total_sum)

# 16. list() - Creates a list from an iterable
new_list = list("hello")
print("16. list('hello'):", new_list)

# 17. Slicing - Accessing parts of the list using slicing
sliced_list = sample_list[1:4]  # Slicing from index 1 to 3
print("17. sample_list[1:4]:", sliced_list)

# 18. List comprehension - Creating a new list based on existing list
squared_list = [x * x for x in sample_list]
print("18. List comprehension (squared):", squared_list)

# 19. any() - Returns True if any element of the list is true
any_true = any([False, True, False])
print("19. any([False, True, False]):", any_true)

# 20. all() - Returns True if all elements of the list are true
all_true = all([True, True, True])
print("20. all([True, True, True]):", all_true)

# 21. enumerate() - Returns an enumerate object that contains the index and value of all items in the list
enumerated_list = list(enumerate(sample_list))
print("21. enumerate(sample_list):", enumerated_list)

# 22. filter() - Filters the list based on a function
filtered_list = list(filter(lambda x: x % 2 == 0, sample_list))
print("22. filter(lambda x: x % 2 == 0, sample_list):", filtered_list)

# 23. map() - Applies a function to all elements in the list
mapped_list = list(map(lambda x: x * 2, sample_list))
print("23. map(lambda x: x * 2, sample_list):", mapped_list)

# 24. zip() - Aggregates elements from two or more iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print("24. zip(list1, list2):", zipped_list)

# 25. del statement - Removes an element by index or slices
del sample_list[0]  # Deletes the first element
print("25. del sample_list[0]:", sample_list)
del sample_list[1:3]  # Deletes elements from index 1 to 2
print("del sample_list[1:3]:", sample_list)

# 26. in operator - Checks if an element exists in the list
is_in_list = 5 in sample_list
print("26. 5 in sample_list:", is_in_list)

# 27. not in operator - Checks if an element does not exist in the list
is_not_in_list = 10 not in sample_list
print("27. 10 not in sample_list:", is_not_in_list)
