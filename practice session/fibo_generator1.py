def fibo():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

g=fibo()

for i in g:
    if i>200:
        break
    print(i)


    

    