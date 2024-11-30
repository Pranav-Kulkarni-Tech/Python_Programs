list1=[22,23,43,21,22,22,55,66]
enm=list(enumerate(list1))
print(enm)

list1.append(1)
print(list1)

#del list1[0]
#print(list1)

c=list1.count(22)
print(c)

list2=[33,44,33,3,22]
list3=list(zip(list1,list2))
print(list3)

slic=list1[1:35]
print(slic)

print(max(list1))


even=list(filter(lambda x:x%2==0,list1))
print(even)

print(sorted(list1))

list2.sort()
print(list2)