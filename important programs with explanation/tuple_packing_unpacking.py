packing_tuple=1,2,3,4

print(packing_tuple) # # Output: (1, 2, 3, 4)

#Packing is when we take multiple values and combine them into a single tuple. This means that Python will automatically pack the values into a tuple


#Unpacking is when we take the values from a tuple and assign them to multiple variables. Each value in the tuple will be assigned to a corresponding variable.
a,b,c,d=packing_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4



# Tuple Packing
packed_tuple = 1, 2, 3, 4, 5, 6  # A tuple with 6 values

# Unpacking with the `*` operator
a, *b = packed_tuple

print(a)  # Output: 1 (first value)
print(b)  # Output: [2, 3, 4, 5, 6] (remaining values as a list)

"""
 Extended Unpacking with * Operator
Sometimes, you might want to unpack only some of the values and pack the remaining values into a list. This is done using the * operator.
"""