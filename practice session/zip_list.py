#Can you provide an example of how to use zip() to combine two lists into a list of tuples?

list1=[1,2,3]
list2=[3,4,5]
list0=[7,8,9]

list3=list(zip(list1,list2,list0))
print(list3)
"""zip() function works by combining two or more iterables (e.g., lists, tuples) into a single iterator of tuples."""




litu = [(1, 'a'), (2, 'b'), (3, 'c')]
print(litu)
list1,list2=zip(*litu)
print(list(list1))
print(list(list2))





list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Output: [1, 2, 3]  ['a', 'b', 'c']

#   * operator can be used to unpack the list of tuples




