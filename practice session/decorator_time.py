import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"fucntion {func.__name__} execute {end-start:.4f} ")
        return result
    return  wrapper

@timer   
def task1():
    time.sleep(2)
    print("task 1 execute")

task1()


    







"""
    1. Importing the time Module
The time module is used to measure the current time using time.time() (returns the number of seconds since the epoch, typically used for timing).
2. Decorator Definition (timer(func))
What does the timer decorator do?
The timer decorator wraps another function and adds timing logic to measure how long the function takes to execute.
Key Points in timer:
func: This is the function to be decorated (e.g., task1).

Wrapper Function:

The wrapper function defines additional behavior (timing, in this case) around the original function.
It accepts arguments (*args and **kwargs) to allow the decorator to work with functions of varying parameter types.
Timing Logic:

start = time.time() records the start time.
The original function (func(*args, **kwargs)) is executed, and its result is stored in result.
end = time.time() records the end time.
Execution Time:

The difference between end and start is calculated (end - start) and printed in the format of seconds with four decimal places (:.4f).
Returning Result:

The original function's result (result) is returned, ensuring the decorator doesn't interfere with the function's behavior.
    """
