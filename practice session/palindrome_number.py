n=int(input("enter a number"))
rev=0
x=n

while n>0:
    rev=(rev*10) +(n%10)
    n=n//10
if x==rev:
    print("palindrome")
else:
    print("not palindrome")

"""
 rev=(rev*10) +(n%10)
    n=n//10
122

rev=0*10 + 122%10
rev=0+ 2
rev=2
n=12

rev= 2*10 + 12%10
rev=20 + 1=21
n=1


rev=21*10 +1%10
rev=210 +0.1





"""
