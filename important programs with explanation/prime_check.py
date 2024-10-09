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

Range Optimization:
Normally, to check if a number is prime, you would check all numbers from 2 to num-1.
However, it's not necessary to check all the way up to num-1 because a larger factor of num would have a smaller corresponding factor.
The largest factor we need to check is the square root of the number (num**0.5). If num has a divisor larger than its square root, the corresponding smaller divisor will have already been found.
Efficient Loop:
range(2, int(num**0.5) + 1) generates numbers starting from 2 up to the square root of num. Adding 1 is needed because range() excludes the upper limit.
This significantly reduces the number of iterations compared to checking all the way to num-1, making the program faster for larger numbers.
Example: For num = 25, instead of checking divisors up to 24, you only need to check up to 5, because if 25 has a factor larger than 5, it would already have a smaller corresponding factor.


Explanation of Corrections:
Correct Loop Range Calculation:

for i in range(2, int(num**0.5) + 1): This correctly calculates the range up to the square root of num. If num can be divided by any number in this range, it is not a prime number.

Proper Handling of Divisibility Check:

The return True statement is outside the for loop, so it only returns True if no divisors are found throughout the entire loop. This means num is confirmed to be prime only if no divisors were found.
"""