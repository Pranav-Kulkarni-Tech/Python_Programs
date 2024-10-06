def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
print(fact(6))


"""

6*fact(5)   6*120=720
5*fact(4)   5*24=120
4*fact(3)   4*6=24
3*fact(2)   3*2=6
2*fact(1)   2*1=2
1*fact(0) 





"""