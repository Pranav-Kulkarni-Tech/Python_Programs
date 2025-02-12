list1=[111,22,23,444,555,665,555,54,553,433,224,115]

del list1[1]
print(list1)



list1.remove(553)
print(list1)

pop_value=list1.pop(1)
print("pop value",pop_value)

del list1[:6]
print(list1)

"""
Key Differences:
del:
Removes elements by index or slice.
Can delete the entire list object.
No return value.

remove():
Removes the first occurrence of a specific value.
Raises a ValueError if the value is not found.
No return value.

pop():
Removes and returns an element by index.
If no index is given, removes and returns the last element.

clear():
Empties the entire list.
No return value.
"""