set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}



set1.add(6)
print("add 6",set1)
print("set1",set1)
print("set2",set2)
cleared_set = set1.copy()
cleared_set.clear()
print("2. clear():", cleared_set)

set3=set1.copy()
set3.clear()

dif=set1.difference(set2)
print("difference",dif)

inter=set1.intersection(set2)
print("intersection",inter)

inter_update=set1.copy()
inter_update.intersection_update(set2)
print("intersection_update",inter_update)

dif_update=set1.copy()
dif_update.difference_update(set2)
print("difference update",dif_update)

is_sub={1,2}.issubset(set1)
print("subset",is_sub)

super_set=set1.issuperset({1,2})
print("superset",super_set)

unionset=set1.union(set2)
print("unionset",unionset)

update_set=set1.copy()
update_set.update(set2)
print("update",update_set)

for ele in set1:
    print(ele)

list1=[1,1,2,2,3,3,4,4,5]
set1=set(list1)
print(set1)


inset= 2 in set1
print("present",inset)