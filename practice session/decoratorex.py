def decorator(func):
    def wrapper():
        print(" wrapper function worked")
        func()
    print("decorator function worked ")
    return wrapper


@decorator
def show():
    print("Show function worked")
show()