import time

def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"starting time is {start} and ending time is {end} of function {func.__name__} is {end-start:.4f}")
        return result
    return wrapper

@timer
def show():
    time.sleep(2)
    print("show function workded")
show()


@timer
def add(a,b):
    print(a+b)
add(5,6)