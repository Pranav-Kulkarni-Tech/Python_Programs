def decorator_func(func):
    def wrapper_fuc():
        print("Wrapper function worked")
        func()
    print("Decorator function worked")
    return wrapper_fuc

@decorator_func
def display():
    print("Display function work")
display()

"""
decorator_func is defined as a function that takes another function func as an argument.
Inside decorator_func, wrapper_fuc is defined to print "Wrapper function worked" and call func.
decorator_func prints "Decorator function worked".
decorator_func returns wrapper_fuc.
"""