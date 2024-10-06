numbers=[1,2,3,4]
square=map(lambda x:x**2,numbers)
print("map use",list(square))

num=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda x:x%2==0,num)
print("even using filter",list(even))


from functools import reduce
r=[2,3,4,55,66,77,88]
re=reduce(lambda x,y:x+y,r)
print("reduce use",re)
