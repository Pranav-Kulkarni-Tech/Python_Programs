def palindrome(s):
    temp=s[::-1]
    if temp==s:
        print("string is palindrome")
    else:
        print("string is not palindrome")

s=input("Enter a string")

palindrome(s)
    
    


