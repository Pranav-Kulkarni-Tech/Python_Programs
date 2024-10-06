def prime_check(num):
    if num<=2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True


def between(start,end):
    prime=[]
    for i in range(start,end):
        if prime_check(i):
            prime.append(i)
    return prime

start=int(input("Enter a starting number"))
end=int(input("Enter ending number"))

all=between(start,end)

print(f"between {start}  and {end} prime  numbers are {all}")

