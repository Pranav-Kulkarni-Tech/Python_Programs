def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True


def find_prime(start,end):
    prime=[]
    for num in range(start,end+1):
        if is_prime(num):
            prime.append(num)
    return prime
        
start=int(input("give starting number"))
end=int(input("end number"))

prime_numbers=find_prime(start,end)
print(f"prime numbers between {start} and {end} is {prime_numbers}")


"""
1. The is_prime(n) Function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
Explanation:
Purpose: This function checks whether a given number n is a prime number.

Step-by-Step:

Check if n is less than or equal to 1:
Prime numbers are defined as numbers greater than 1 that are only divisible by 1 and themselves. Therefore, any number less than or equal to 1 is not prime.
If n is less than or equal to 1, the function returns False.
Loop through possible divisors:
The function checks divisibility from 2 up to the square root of n. The reason for stopping at the square root is that if n can be divided evenly by a number larger than its square root, the corresponding divisor will be smaller than the square root. Thus, checking up to the square root is sufficient.
The loop for i in range(2, int(n**0.5) + 1): generates numbers from 2 up to the integer value of the square root of n (plus 1 to include the square root).
Check divisibility:
Inside the loop, the code checks if n is divisible by i using the modulus operator %. If n % i == 0, then n is not a prime number (it has a divisor other than 1 and itself).
If a divisor is found, the function immediately returns False, indicating that n is not prime.
Return True if no divisors are found:
If the loop completes without finding any divisors, the function returns True, indicating that n is a prime number.
2. The find_prime(start, end) Function

def find_prime(start, end):
    prime = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime.append(num)
    return prime
Explanation:
Purpose: This function finds all prime numbers within a specified range (start to end).

Step-by-Step:

Initialize an empty list:

The function starts by creating an empty list called prime. This list will store all the prime numbers found within the given range.
Loop through the range:

The function uses a for loop to iterate through every number in the range from start to end (inclusive). The range function range(start, end + 1) ensures that the loop covers all numbers from start to end.
Check if the number is prime:

For each number num in the range, the function calls is_prime(num) to check if it is a prime number.
If is_prime(num) returns True, the number is added to the prime list using the append() method.
Return the list of prime numbers:

After the loop finishes, the function returns the prime list, which contains all the prime numbers found between start and end.
3. The Main Program

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_numbers = find_prime(start, end)
print(f"Prime numbers between {start} and {end} are: {prime_numbers}")
Explanation:
Purpose: This is the main part of the program that interacts with the user, calls the find_prime() function, and displays the result.

Step-by-Step:

User Input:
The program asks the user to enter the starting and ending numbers for the range. These values are stored in the variables start and end.
Call the find_prime() function:
The program calls find_prime(start, end) to find all prime numbers between start and end. The result is stored in the variable prime_numbers.
Display the result:
The program prints the list of prime numbers found, using a formatted string to display the result in a user-friendly way.
Example Execution:
If the user inputs start = 10 and end = 20, the program will:
Call find_prime(10, 20).
Inside find_prime(), check each number from 10 to 20 to see if it is prime.
Identify 11, 13, 17, and 19 as prime numbers.
Return the list [11, 13, 17, 19].
The program then prints: Prime numbers between 10 and 20 are: [11, 13, 17, 19].
This program efficiently finds and lists all prime numbers in a given range, while the is_prime function ensures that only numbers with no divisors other than 1 and themselves are identified as prime.
"""

