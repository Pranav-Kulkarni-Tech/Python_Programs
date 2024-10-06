#why list mutable  and tuple are immutable

list1=[1,2,3]
list2=[4,5,6]
print("list1 id is",id(list1))
print(list1)
print("list2 id is",id(list2))
print(list2)
list1.extend(list2)
print(list1)

print("list1 id is",id(list1))

tuple1=(11,12,13)
print("tuple1 id ",id(tuple1))
tuple2=(14,15,16)
print("id of tuple2",id(tuple2))
tuple1=tuple1+tuple2
print("tuple1 id",id(tuple1))
print(tuple1)

"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("list1 id is", id(list1))  # Print the memory address of list1
print(list1)                     # Print the contents of list1

print("list2 id is", id(list2))  # Print the memory address of list2
print(list2)                     # Print the contents of list2

list1.extend(list2)               # Add elements of list2 to the end of list1
print(list1)                       # Print the modified list1

print("list1 id is", id(list1))  # Print the memory address of list1 (unchanged)

tuple1 = (11, 12, 13)
print("tuple1 id ", id(tuple1))     # Print the memory address of tuple1

tuple2 = (14, 15, 16)
print("id of tuple2", id(tuple2))   # Print the memory address of tuple2

tuple1 = tuple1 + tuple2          # Create a new tuple by concatenating
print("tuple1 id", id(tuple1))     # Print the memory address of the new tuple (different)
print(tuple1)                     # Print the contents of the new tuple

"""