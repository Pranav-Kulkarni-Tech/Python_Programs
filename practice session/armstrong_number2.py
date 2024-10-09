def armstrong(num):
    
    digit=str(num)
    length=len(digit)
    sumof=sum(int(dg)**length for dg in digit)
    return sumof==num




num=int(input("Enter a number"))

if armstrong(num):
    print(f"{num} is armstrong")
else:
    print(f"{num} is not armstrong")