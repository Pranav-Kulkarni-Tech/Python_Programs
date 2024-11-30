import copy

list1=[1,[2,3],4]
list2=copy.copy(list1)   # shallow copy
list1[1][0]=100   #  Modify inner list in list1
print(list2)   #  Output:  [1, [100, 3], 4]


import copy
list1 = [1, [2, 3], 4]
list3 = copy.deepcopy(list1)  #  Deep copy

list1[1][0] = 100  #  Modify inner list in list1
print(list3)       # Output: [1, [2, 3], 4]



"""
1. Shallow Copy
Definition: A shallow copy creates a new object, but only copies the references to the objects within the original object. It doesn’t create a copy of the nested objects themselves.

Effect: Changes made to mutable objects inside the original object (like lists or dictionaries) will also reflect in the shallow copy, since both refer to the same memory location for those inner objects.


2. Deep Copy
Definition: A deep copy creates a new object and recursively copies all the objects inside the original object, meaning even the nested objects get copied. Each object is fully independent.

Effect: Changes made to the original object will not affect the deep copy and vice versa, even if they contain mutable nested objects.
"""