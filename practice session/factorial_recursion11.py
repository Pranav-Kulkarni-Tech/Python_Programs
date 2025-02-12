def fact(num):
    if num<=1:
        return 1
    return num * fact(num-1)
num=int(input("enter a number"))
print(fact(num))