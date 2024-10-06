def fibo():
    first,second=0,1
    while True:
        yield first
        first, second = second, first + second

        
g=fibo()

for  i in g:
    if i>=100:
        break
    print(i)
