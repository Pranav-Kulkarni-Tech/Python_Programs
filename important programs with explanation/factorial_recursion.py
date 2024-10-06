def fact(n):
    if n<=1:  #Base case
        return 1
    else:
        return n*fact(n-1) # Recusrive function
print(fact(4))

"""


def fact(n):                        
    if n<=1:
        return 1
    return n*fact(n-1)      n=1 
fact(1)

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)   n=2   n*fact(1)         2*1=2
fact(2)

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)   n=3   n*fact(2)         3*2=6
fact(3)

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)    n=4  n*fact(3)              4*6=24
fact(4)


"""