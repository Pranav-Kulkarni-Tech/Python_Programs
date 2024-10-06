def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)
n=int(input("Enter how many terms you want in fibonacci series"))
if n<0:
    print("please enter positive nuumber")
else:
    for i in range(n):
        print(fibo(i))

"""

def fibo(n):               
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)
n=int(input("Enter how many terms you want in fibonacci series"))
if n<0:
    print("please enter positive nuumber")
else:
    for i in range(n):
        print(fibo(i))

        


n=0     return 0              n=0
 n=1   return 1               n=1
n=2       fib(1)+fib(0)      1+0=1  
n=3        fib(2) +fib(1)    1+1=2
n=4        fib(3)+fib(2)         2+1=3
                              
                             
"""
