list1=[1,3,53,22,2,44,45,54]

largest=max(list1)
list1.remove(largest)


second_largest=max(list1)
print(f" {second_largest} is second largest element ")


#using sort method

large=list1.sort()

second_largest_element=large[-2]
print("second largest element using sort and slicing",second_largest_element)