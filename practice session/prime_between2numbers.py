def prime_num(num):
    if num<1:
        return False
    else:
        for i in range(2,int(num*0.5)+1):
            if num%i==0:
                return False
            
        return True
    
def bet_prime(start,end):
    prime=[]
    for i in range(start,end+1):
        if prime_num(i):
            prime.append(i)
    return prime

start=int(input("Enter a starting number"))
end=int(input("Enter ending number"))


prime_list=bet_prime(start,end)
print(f" prime numbers between {start} and {end} is {prime_list}")