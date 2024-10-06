def fact(n):
    if n<=1: # base case
        return 1
    return n*fact(n-1) #recursive case

n=int(input("Enter a number"))

print(fact(n))