def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

n=int(input("Enter How many number you want"))
if n<=0:
    print("please enter a positive number")
else:
    for i in range(n):
        print(fibo(i))