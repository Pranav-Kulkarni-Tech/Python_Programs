def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r

n=int(input("enter a number"))


print(f"{fact(n)} is value")