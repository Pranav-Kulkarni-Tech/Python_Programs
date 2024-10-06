def prime_num(n):
    if n<=1:
        return False
    for i in range(2,int(0.5*n)):
        if n%i==0:
            return False
    return True

def is_prime(start,end):
    prime=[]
    for num in range(start,end+1):
        if prime_num(num):
            prime.append(num)
    return prime
        
start=int(input("enter a starting number"))
end=int(input("Enter a ending number"))

prime_numbers=is_prime(start, end)
print(f"prime number between {start}  {end} is {prime_numbers}")





