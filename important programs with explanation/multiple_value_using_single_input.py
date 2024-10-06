# read Multiple value using single input

x=list(map(int,input("Enter a value ").split()))
print("values of x is", x)

#x=[int(x) for x in input("Enter a value: ").split()]
# print("values of x is ",x)
x=tuple(map(int,input("Enter a value ").split()))
print("values of x is", x)