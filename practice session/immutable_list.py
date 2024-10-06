list1=[1,2,3,4,5,6]
list2=[8,9,88,77,66]

print("list1",id(list1))
print("list2",id(list2))

list1.extend(list2)
print("list1 id after extend",id(list1))


tuple1=(1,2,3)
tuple2=(4,5,6)

print("tuple1",id(tuple1))
print("tuple2",id(tuple2))

tuple1=tuple1+tuple2
print("tuple1",id(tuple1))