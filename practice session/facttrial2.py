def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

n=int(input("enter a number"))
print(fact(n))

"""
1*1=1

1*2=2
2*3=6

6*4=24


"""