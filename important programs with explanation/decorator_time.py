import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"Functon {func.__name__} executed in {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def task1():
    time.sleep(2)
    print("task1 finished")

task1()

"""
Decorator is function which takes another function as an argument, add some functionality to it, and return another function

Built-in Decorators in Python
@staticmethod: Converts a method into a static method.
@classmethod: Makes a method act on the class rather than an instance.
@property: Allows you to access methods as if they were attributes.

Advantages of Decorators
Code Reusability: Common functionality can be applied across functions without duplication.
Separation of Concerns: Keeps core logic separate from additional behaviors.
Readability: Makes code more concise and easier to understand.
Extensibility: You can easily modify behaviors without touching the original function.

 points of a Decorator:
The Wrapper Function:

The inner function (wrapper) is where the additional behavior is defined. It wraps the target function.
The *args and **kwargs:

These allow the decorator to work with any function signature by passing all arguments through to the wrapped function.
Returning the Wrapper:

The decorator function must return the wrapper so that the original function is replaced by the decorated one.

Use Cases of Decorators
Logging: Tracking the execution of functions.
Authentication: Ensuring users have the right permissions before executing a function.
Timing: Measuring how long a function takes to execute.
Debugging: Adding diagnostic output for development.
Caching: Storing results of expensive computations for faster retrieval




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