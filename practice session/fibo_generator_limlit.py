import sys
def fibo():
    a,b=0,1
    count=0
    while count<4:
        yield a
        a,b=b,a+b
        count+=1
g=fibo()
for i in g:
    print(i)

print("Memory size is ", sys.getsizeof(g))