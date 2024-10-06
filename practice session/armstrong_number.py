def armstrong(num):
    string=str(num)
    length=len(string)
    sum_of=sum(int(st)** length for st in string )
    print(sum_of)
    return sum_of==num
n=153
if armstrong(n):
    print(f"{n} is armstrong number" )
else:
    print(f"{n} is not armstrong number")

    """
    153=
    
    """