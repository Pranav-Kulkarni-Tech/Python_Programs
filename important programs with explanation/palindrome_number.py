n=int(input("Enter a number"))
x=n
rev=0
while n>0:
    rev=(rev*10) + n%10
    n=n//10
if x==rev:
    print("is palindrome number")
else:
    print("is  not plaindrome")

"""

rev=(rev*10) + n%10
    n=n//10
n=121

rev=0*10 + 121%10    0+1=1 rev=1
n=121//10= 12     

rev=1*10  + 12%10  =10 +2=12
n=12//10= 1

here while n>0 false so we write  1 as it is
rev=12*10  + 1%10 =  120+1=121





Introduction: This program checks whether a given number is a palindrome. A palindrome number reads the same forward and backward.

Explanation of Variables:

rev starts at 0 and will store the reversed number.
x holds the original value of num to compare later.
While Loop Logic:

The condition while num > 0 ensures the loop continues until all digits of num are processed.
Inside the loop:
rev = (rev * 10) + num % 10: This multiplies rev by 10 to shift digits and adds the remainder of num divided by 10 (extracting the last digit).
num = num // 10: This reduces num by removing its last digit (integer division).
Comparison:

After the loop, rev contains the reversed number.
The program compares rev to x (the original number).
If they are equal, the number is a palindrome; otherwise, it’s not.

"""

