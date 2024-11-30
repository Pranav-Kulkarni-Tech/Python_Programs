
#How would you sort a list of tuples based on the second element of each tuple?
list1=[(33,111),(4,12),(7,14),(5,3)]
sorting=sorted(list1,key=lambda x:x[1])
print(sorting)

sorting_first=sorted(list1, key=lambda x:x[0])
print("sorting first",sorting_first)