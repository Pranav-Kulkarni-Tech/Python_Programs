def is_prime(num, divisor=2):
    # Check if num is less than or equal to 1
    if num <= 1:
        return False
    
    # Check if divisor squared is greater than num
    if divisor * divisor > num:
        return True

    # Check if num is divisible by divisor
    if num % divisor == 0:
        return False
    
    # Recursive call to check the next divisor
    return is_prime(num, divisor + 1)


num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")



"""

if num <= 1:
    return False
If the number (num) is less than or equal to 1, it's not a prime number. The function returns False immediately.
Base Condition 2: Divisor Exceeds Square Root

if divisor * divisor > num:
    return True
The divisor starts at 2.
If the square of the divisor exceeds the number (divisor * divisor > num), the function returns True. This is because, at this point, the number can't have any divisors other than 1 and itself.
Base Condition 3: Is num Divisible by divisor?

if num % divisor == 0:
    return False
If the number is divisible by the current divisor (num % divisor == 0), it means the number has a divisor other than 1 and itself, so it's not prime, and the function returns False.
Recursive Call: Increment Divisor

return is_prime(num, divisor + 1)
If none of the above conditions are met, the function calls itself recursively, incrementing the divisor by 1, i.e., divisor + 1.
This process continues until either the number is found divisible by a divisor or the divisor squared exceeds the number.
Example Walkthrough for num = 29
The user inputs 29. num is 29.
The function starts with divisor = 2.
First check: Is 29 <= 1? No, so it moves to the next check.
Second check: Is 2 * 2 > 29? No, so it moves to the next check.
Third check: Is 29 % 2 == 0? No, so the function calls itself with divisor = 3.
The function now runs with num = 29 and divisor = 3.
First check: Is 3 * 3 > 29? No, so it continues.
Third check: Is 29 % 3 == 0? No, so it calls itself again with divisor = 4.
The function keeps increasing the divisor, repeating the checks for divisors 4, 5, and so on.

When divisor = 6, the check 6 * 6 > 29 becomes True, so the function returns True since no divisor has successfully divided 29. This confirms that 29 is a prime number.
"""