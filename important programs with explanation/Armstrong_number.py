def armstrong(num):
    digits=str(num)
    num_digit=len(digits)
    sum_of_powers=sum(int(digit)** num_digit for digit in digits)
    return sum_of_powers==num
n=int(input("Enter a number"))

if armstrong(n):
    print(f" {n} is armstrong")
else:
    print(f" {n} is not armstrong")

"""
Function Signature:

def armstrong(num):
This line defines a function named armstrong that takes a single parameter num.
Convert Number to String:

digits = str(num)
The integer num is converted to a string. This allows easy iteration over each digit. For example, if num is 153, then digits will be '153'.
Calculate Number of Digits:

num_digit = len(digits)
This calculates the length of the string digits, which gives the number of digits in the number. For instance, for 153, num_digit will be 3.
Sum of Powers of Digits:

sum_of_powers = sum(int(digit) ** num_digit for digit in digits)
This line does the following:
Iterates over each digit in the string digits.
Converts each digit back to an integer.
Raises the digit to the power of num_digit.
Sums all these values together.
For example, for 153, this calculation will be:
1^3 + 5^3 + 3^3
1 + 125 + 27
153
Return Comparison Result:

return sum_of_powers == num
This checks if the calculated sum_of_powers is equal to the original num.
If they are equal, the function returns True, indicating that num is an Armstrong number.
Otherwise, it returns False.


User Input:

n = int(input("Enter a number: "))
This line prompts the user to enter a number.
The input is read as a string and then converted to an integer, which is stored in the variable n.
Check Armstrong Number and Print Result:

if armstrong(n):
This calls the armstrong function with n as the argument.
If the function returns True, indicating n is an Armstrong number, the following line executes:
print(f"{n} is an Armstrong number.")
Otherwise, the else block executes:
print(f"{n} is not an Armstrong number.")
Summary
Definition: The code defines a function armstrong that checks whether a given number is an Armstrong number by calculating the sum of its digits each raised to the power of the number of digits and comparing it to the original number.
Steps:
Convert the number to a string to easily iterate over its digits.
Calculate the number of digits.
Compute the sum of each digit raised to the power of the number of digits.
Compare the computed sum with the original number.
User Interaction: The code prompts the user to enter a number, checks if it is an Armstrong number using the armstrong function, and prints the result.


"""