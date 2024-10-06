#palindrome number 

n=int(input("Enter anumber"))
rev=0
x=n
while n>0:
    rev=(rev*10) + n%10
    n=n//10 
if x==rev:
    print("palindrome")
else:
    print("not palindrome")
    
