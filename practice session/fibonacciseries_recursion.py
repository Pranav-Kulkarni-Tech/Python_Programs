def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+ fibo(n-2)

n=int(input("enter a numbers you want in series"))

if n<=1:
    print("enetr valid number")
else:
    for i in range(n):
        print(fibo(i))