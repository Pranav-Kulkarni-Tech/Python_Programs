def fibo(n):
    if n<=1:
        return 1
    return fibo(n-1)+fibo(n-2)
n= int(input("Enter a number"))
if n<=1:
    print("Enter positive number")
else:
    for i in range(n):
        print(fibo(i))