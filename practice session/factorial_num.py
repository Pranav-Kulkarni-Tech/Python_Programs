def fact(n):
    if n<1:
        return 1
    return n* fact(n-1)

print(fact(4))

"""
fact(4)= 4*fact(3)=4*6=24
fact(3)= 3*fact(2)= 3*2=6
fact(2)= 2*fact(1)=2*1=2
fact(1)= 1*fact(0)= 1

"""
