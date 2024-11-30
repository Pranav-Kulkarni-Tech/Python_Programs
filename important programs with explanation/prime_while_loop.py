def prime(num):
    if num<=1:
        return False
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i=i+1
    
    return True


num=int(input("Enter a number"))
if prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} not prime")