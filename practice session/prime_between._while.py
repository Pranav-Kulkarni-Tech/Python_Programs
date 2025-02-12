def prime(num):
    if num<1:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i=i+1
    return True

num=int(input("enter a number"))
if prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime")