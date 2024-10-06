num=int(input("enter a number"))
if num<=1:
    print("Enter a positive number")
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break

    if is_prime:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number")


"""
range(2, int(num**0.5) + 1) creates a range of numbers starting from 2 up to the square root of num, inclusive.
The +1 ensures that the square root itself is included in the range. For num = 36, the range will be 2, 3, 4, 5, 6.

1. Input Handling

num = int(input("Enter a number: "))
Explanation: The code starts by asking the user to input a number, which is then converted into an integer. This number (num) is the one we will check to see if it's prime.
2. Handling Edge Cases

if num <= 1:
    print(f"{num} is not a prime number.")
Explanation: Prime numbers are defined as being greater than 1. So, if the user enters a number less than or equal to 1, the code immediately concludes that it's not a prime number and prints a message. This is a quick way to handle inputs like 0, 1, or negative numbers.

3. Assuming the Number is Prime

else:
    is_prime = True
Explanation: If the number is greater than 1, the code initially assumes it is a prime number by setting a variable is_prime to True. This is a common strategy—start by assuming something is true and then look for evidence to prove otherwise.
4. Checking for Divisibility

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
Explanation:
Loop Range: The for loop runs from 2 to the square root of num (plus one). The reason for this range is that if a number num has a divisor other than 1 and itself, one of those divisors will be less than or equal to the square root of num. This makes the check more efficient, especially for larger numbers.

Divisibility Check: Inside the loop, the code checks if num is divisible by any i within the range. If it is (num % i == 0), then num is not a prime number, so is_prime is set to False, and the loop is exited using break.

5. Final Decision

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
Explanation: After the loop, the code checks the value of is_prime. If it's still True, the number is prime, and a message is printed to that effect. If it’s False, the number is not prime, and the corresponding message is printed.
Overall Summary
Purpose: This code efficiently determines if a given number is prime by checking for divisibility only up to the square root of the number.
Key Points:
Handles edge cases (like numbers ≤ 1).
Uses an optimized loop to reduce the number of checks needed.
Makes a clear decision based on the results of the loop.
 """       