import copy
list1=[1,2,[3,4],5]

list2=copy.copy(list1)

list1[2][1]=9

print("list1",list1)

print("list2", list2)


list3=copy.deepcopy(list1)

list1[2][1]=88
print(list1,"deepcopy list1")
print(list3,"list3 ") 