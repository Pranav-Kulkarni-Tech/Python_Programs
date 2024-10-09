
# [expression for item in iterable if conditional]

square=[2,4,5,6,7,8]
square=[x**2 for x in square]
print("square",square)

even=[x for x in square if x%2==0]
print(even)

#square  1 to 11
# {key:value for (key,value) in iterable if conditional}
d={}
d={x:x**2 for x in range(12)}
print(d)

k={}
k={x:x+10 for x in range(2,140) if x%2}
print(k)


#Set comprehension
set_of={x for x in range(2,78) if x%2!=0}
print(set_of) 


#tuple comprehension
tu=tuple(x**5 for x in range(9,199)if x%2==0)
print("tuple ",tu)