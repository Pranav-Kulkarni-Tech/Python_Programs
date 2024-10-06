def armstrong(num):
    digits=str(num)
    le=len(digits)
    power_sum=sum(int(digit) ** le for digit in digits)
    return power_sum==num
n=int(input("Enter a number"))

if armstrong(n):
    print(f"{n} armstrong number")
else:
    print(f"{n} not armstrong number ")