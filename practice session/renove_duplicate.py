list1=[1,1,12,22,22,12,3,4,5,3,4,5]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)