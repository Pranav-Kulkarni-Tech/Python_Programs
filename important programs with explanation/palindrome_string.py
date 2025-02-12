string=input("Enter a string")
if string==string[::-1]:
    print(" string is palindrome")
else:
    print("not palindrome")

"""
"In this program, we check whether a given string is a palindrome using string slicing. A palindrome is a string that reads the same forward and backward.

We take input from the user and compare the original string with its reversed version using [::-1]. This slicing method reverses the string by starting from the end and moving to the beginning.

If both strings are identical, we print that the string is a palindrome. Otherwise, we print that it is not a palindrome."
"""




