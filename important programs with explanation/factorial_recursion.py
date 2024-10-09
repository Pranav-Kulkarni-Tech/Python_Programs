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



Each recursive call creates a new instance of the function on the call stack:

When a function calls itself within its own definition, it effectively creates a new instance of the function, with its own set of local variables and arguments.
This new instance is pushed onto the call stack, a temporary memory area that keeps track of the program's current execution state.
You can think of it as a stack of plates, where each new function call adds a new plate on top of the stack.
During recursion, execution of each function is paused until the current recursive call returns:

When a function makes a recursive call, its own execution is temporarily suspended, and the function's state (local variables, arguments) is stored on the call stack.
Once the base case is reached (the condition that terminates the recursion), the function starts returning values.
As the recursive calls return, the suspended functions resume execution, using the returned values to complete their operations.
"""