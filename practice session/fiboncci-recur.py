def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+ fibo(n-2)

n=int(input("numbers in fibonacci series"))
if n<0:
    print("Please enter positive number")
else:
    for i in range(n):
        print(fibo(i))
