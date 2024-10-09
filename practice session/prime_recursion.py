def prime(num,divisor=2):
    
    if num<=1:
        return False
    
    if divisor*divisor>num:
        return True
    
    if num%divisor==0:
        return False
    
    return prime(num,divisor+1)
    
num=int(input("Enter a number"))

if prime(num):
    print(f"{num} is prime")

else:
    print(f"{num} is not prime")
