
"""
def palindrome(n):
    temp=n[: :-1]
    if temp==n:
        print("string is palindrome")
    else:
        print(f"{n} string is not palindrome")
palindrome('pranav')
"""


"""
s='raj'

temp=s[: :-1]
if temp==s:
    print("palindrome")
else:
    print("not palindrome")
    """

# using indexing

s=input("enter string")
a=len(s)
for i in range(a):
    temp=s[a-i-1]
if temp==s[i]:
    print("palindrome")
else:
    print("not palindrome")