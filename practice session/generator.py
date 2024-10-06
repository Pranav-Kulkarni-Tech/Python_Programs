import sys
def fibo():
    a,b=0,1
    count=0
    while count<=100:
        yield a
        a,b=b,a+b
        count=count+1
g=fibo()
for i in g:
    print(i)
print("size is",sys.getsizeof(g))
