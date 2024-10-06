def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
            
    return True

num=int(input("enter number"))
if prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


"""
Explanation of Corrections:
Correct Loop Range Calculation:

for i in range(2, int(num**0.5) + 1): This correctly calculates the range up to the square root of num. If num can be divided by any number in this range, it is not a prime number.

Proper Handling of Divisibility Check:

The return True statement is outside the for loop, so it only returns True if no divisors are found throughout the entire loop. This means num is confirmed to be prime only if no divisors were found.
"""