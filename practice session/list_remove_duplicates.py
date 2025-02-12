list1=[3,3,22,22,34,5,4,4,3]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
