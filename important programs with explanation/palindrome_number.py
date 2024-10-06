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




"""

