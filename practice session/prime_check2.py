def prime(num):
    if num<=0:
        return False
    else:
        for i in range(2,int(num*0.5)+1):
            if num%i==0:
                return False
            
        return True
                
           
num=int(input("Enter prime number"))

if prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

    