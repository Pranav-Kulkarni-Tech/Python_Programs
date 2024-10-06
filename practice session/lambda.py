a=lambda a:a*a
print(a(8))

num=[1,2,3,4,5,6,7,8,9]

even=filter(lambda x:x%2==0,num)
print(list(even))

odd=filter(lambda x:x%2!=0,num)
print(tuple(odd))

mul=map(lambda x:x*5,num)
print(list(mul))

from functools import reduce
su=reduce(lambda x,y:x+y,num)
print(su)


