def decorator_func(func):
    def wrapper_func():
        print("Wrapper function work")
        func()
    print("decorator function worked")
    return wrapper_func


@decorator_func
def show():
    print("Show function work")
show()

"""
decorator_func is defined as a function that takes another function func as an argument.
Inside decorator_func, wrapper_fuc is defined to print "Wrapper function worked" and call func.
decorator_func prints "Decorator function worked".
decorator_func returns wrapper_fuc.
"""