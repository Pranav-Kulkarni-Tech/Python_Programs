l=[1,2,3,4,6,7,8]
a=filter(lambda x:x%2,l)
print(list(a))

m=[3,2,7,4,5,9]
ex=map(lambda x:x**4,m)
print(list(ex))


from functools import reduce

re=reduce(lambda x,y:x*y,m)
print(re)