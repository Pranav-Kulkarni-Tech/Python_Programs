def fibo():
    a=0
    b=1
    yield a
    count=0
    while count<20:
        a,b=b,a+b
        count=count=1
    
g=fibo()
for i in g:
    print(i)