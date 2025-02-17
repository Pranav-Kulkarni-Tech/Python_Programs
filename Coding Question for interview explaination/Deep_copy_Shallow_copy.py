import copy
list1=[11,12,13,[14,15],16,17]
shallow=copy.copy(list1)

list1[3][0]=90

print("original list",list1) #original list [11, 12, 13, [90, 15], 16, 17]
print("shaloow list",shallow) #shaloow list [11, 12, 13, [90, 15], 16, 17] 



list2=[21,22,23,24,[25,26,27,29],30]
deep=copy.deepcopy(list2)
list2[4][3]=50 

print("list2",list2)    #list2 [21, 22, 23, 24, [25, 26, 27, 50], 30]
print("deep copy",deep) #deep copy [21, 22, 23, 24, [25, 26, 27, 29], 30]

"""
We create list1 and then make a shallow copy of it, storing it in the variable shallow. In list1, we have a nested list [14, 15] at index 3. When we modify the first element of this nested list (changing 14 to 90), the change is reflected in both list1 and shallow. This happens because a shallow copy only creates a new outer list, but the nested objects inside it still share the same memory reference.

On the other hand, we create list2 and make a deep copy of it, storing it in the variable deep. In list2, we have a nested list [25, 26, 27, 29] at index 4. When we modify the last element of this nested list (changing 29 to 50), the change is reflected only in list2, but deep remains unchanged. This is because a deep copy creates completely independent copies of all objects, including nested ones.

So, in summary:

A shallow copy creates a new outer object but keeps references to nested objects. Changes to nested objects affect both copies.
A deep copy creates entirely new copies of all objects, including nested ones, so changes in one object do not affect the other.
"""







