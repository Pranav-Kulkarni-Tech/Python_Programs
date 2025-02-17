#Can you provide an example of how to use zip() to combine two lists into a list of tuples?

list1=[1,2,3]
list2=[3,4,5]
list0=[7,8,9]

list3=list(zip(list1,list2,list0))
print(list3) #[(1, 3, 7), (2, 4, 8), (3, 5, 9)]
"""zip() function works by combining two or more iterables (e.g., lists, tuples) into a single iterator of tuples."""




litu = [(1, 'a'), (2, 'b'), (3, 'c')]
print(litu)
list1,list2=zip(*litu)
print(list(list1)) # [1, 2, 3]
print(list(list2)) # ['a', 'b', 'c']

#   To unzip a zipped object, we use the asterisk (*) operator, which extracts elements into separate iterables.
# The * (asterisk) operator is used to unpack an iterable (like a list of tuples) into separate arguments. When applied to zip(), it helps unzip the data.



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]




list1 = [1, 2]
list2 = ['a', 'b', 'c']

print(list(zip(list1, list2)))  #[(1, 'a'), (2, 'b')]
#If the input iterables have different lengths, zip() stops at the shortest iterable.




