def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(0.5*n)+1):
        if n%i==0:
            return False
        
    return True

def prime_num(start,end):
    prime=[]
    for num in range(start,end+1):
        if is_prime(num):
            prime.append(num)
    return prime
        
start=int(input("enter a starting number"))
end=int(input("enter a ending number"))

prime_numbers=prime_num(start,end)     
print(f" numbers between {start} and {end} is {prime_numbers}") 
