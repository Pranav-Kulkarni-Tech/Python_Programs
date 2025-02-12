def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+ fibo(n-2)

n=int(input("enetr how many numbers in fibonacci you want"))

if n<0:
    print("wrong input")
else:
    for i in range(n):
        print(fibo(i))