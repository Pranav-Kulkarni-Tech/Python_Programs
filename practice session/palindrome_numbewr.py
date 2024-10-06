def palindrome(num):

    rev=0
    x=num
    while num>0:
        rev=(rev*10) + (num%10)
        num=num//10
        
    if x==rev:
        print(f"{x} is palindrome")
    else:
        print(f"{x} is not plaindrome")

num=int(input("enter a number"))

palindrome(num)
