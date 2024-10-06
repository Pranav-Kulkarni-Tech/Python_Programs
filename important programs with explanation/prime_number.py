n=int(input("enter number"))
if n<=1:
    print("enter positive number")
else:
    is_prime=True
    for i in range(2,n):
        
        if(n%i)==0:
            is_prime=False
            break
                       
    if is_prime:
        print(f"{n} prime number")
    else:
        print(f"{n} not prime number")
            

