def divide_numbers():
    try:
# Taking input from the user
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        
# Attempting division
        result = num1 / num2
        print(f"Result of division: {result}")
    
    except ZeroDivisionError:
# Handling division by zero
        print("Error: You cannot divide by zero.")
    
    except ValueError:
# Handling invalid input (e.g., if the user enters a string)
        print("Error: Please enter valid numbers.")
    
    except Exception as e:
 # Handling any other unforeseen exceptions
        print(f"An unexpected error occurred: {e}")
    
    else:
# Executes only if no exceptions occur
        print("Division performed successfully.")
    
    finally:
# Executes regardless of what happens in try/except
        print("Execution completed.")

# Call the function
divide_numbers()



"""
Purpose of exception handling:
The primary purpose of exception handling is to prevent the program from crashing when an error occurs. It gives us a way to respond to errors gracefully and allows the program to continue or stop in a controlled manner.

try block contains code that might raise an exception.

except block catches specific exceptions and handles them.

else block runs if no exceptions are raised in the try block.

finally block runs regardless of exceptions and is usually used for cleanup.
Custom exceptions can be created to handle specific conditions.

Use the finally block for cleanup:
When working with external resources (like files or database connections), the finally block should be used to close them properly.


File Handling: To ensure files are closed properly, even if an error occurs while reading/writing.
Database Connections: To close connections or release cursors, preventing memory leaks or locked resources.
Network Resources: To close sockets or release other network-related resources like HTTP requests.
Cleanup Code: When dealing with resources that need to be reset or released regardless of the outcome of the code execution.







In Python, exceptions are types of errors that occur during the execution of a program, disrupting the normal flow of the program. Each error type has a corresponding exception class. When something goes wrong, Python raises these exceptions, which you can handle using try-except blocks.

Here's an overview of the most common exceptions in Python, their causes, and how to handle them:

---

### **1. `SyntaxError`:**
- **Cause:** Raised when Python encounters invalid syntax. This usually happens when there's a typo or syntax mistake in the code.
- **Example:**
  ```python
  if True
      print("Hello")
  ```
  - The colon `:` is missing, so this would raise a `SyntaxError`.

- **How to handle:** Fix the syntax in the code.

---

### **2. `TypeError`:**
- **Cause:** Raised when an operation or function is applied to an object of inappropriate type. This occurs when incompatible types are used together, like trying to add a string to an integer.
- **Example:**
  ```python
  result = "abc" + 1
  # TypeError: can only concatenate str (not "int") to str
  ```

- **How to handle:** Ensure that the types you are using are compatible (e.g., convert the integer to a string if needed).

---

### **3. `ValueError`:**
- **Cause:** Raised when a function receives an argument of the right type but an inappropriate value.
- **Example:**
  ```python
  num = int("abc")
  # ValueError: invalid literal for int() with base 10: 'abc'
  ```

- **How to handle:** Validate input values before using them in operations.

---

### **4. `IndexError`:**
- **Cause:** Raised when trying to access an index in a list or tuple that doesn't exist.
- **Example:**
  ```python
  my_list = [1, 2, 3]
  print(my_list[5])  
  # IndexError: list index out of range
  ```

- **How to handle:** Ensure that the index is within the valid range of the list or sequence.

---

### **5. `KeyError`:**
- **Cause:** Raised when trying to access a dictionary with a key that doesn't exist.
- **Example:**
  ```python
  my_dict = {"name": "Alice"}
  print(my_dict["age"])  
  # KeyError: 'age'
  ```

- **How to handle:** Check if the key exists before accessing it or use the `get()` method to avoid this exception.
  ```python
  print(my_dict.get("age", "Key not found"))
  ```

---

### **6. `ZeroDivisionError`:**
- **Cause:** Raised when attempting to divide a number by zero.
- **Example:**
  ```python
  result = 10 / 0  
  # ZeroDivisionError: division by zero
  ```

- **How to handle:** Check if the divisor is zero before performing the division.
  ```python
  if divisor != 0:
      result = 10 / divisor
  ```

---

### **7. `AttributeError`:**
- **Cause:** Raised when an invalid attribute reference or assignment is made. This happens when an attribute or method is called on an object that doesn’t support it.
- **Example:**
  ```python
  my_list = [1, 2, 3]
  my_list.append(4)  
  # AttributeError: 'list' object has no attribute 'append2'
  ```

- **How to handle:** Ensure that you're calling valid methods or attributes that exist for that object.

---

### **8. `ImportError` and `ModuleNotFoundError`:**
- **Cause:** Raised when an import statement fails. `ModuleNotFoundError` is a subclass of `ImportError` that occurs specifically when a module can't be found.
- **Example:**
  ```python
  import non_existent_module  
  # ModuleNotFoundError: No module named 'non_existent_module'
  ```

- **How to handle:** Ensure that the module you're trying to import is installed and accessible.

---

### **9. `FileNotFoundError`:**
- **Cause:** Raised when trying to open a file that does not exist.
- **Example:**
  ```python
  with open("non_existent_file.txt") as f:
      content = f.read()
  # FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
  ```

- **How to handle:** Check if the file exists before opening it or use exception handling.
  ```python
  try:
      with open("file.txt") as f:
          content = f.read()
  except FileNotFoundError:
      print("File not found!")
  ```

---

### **10. `NameError`:**
- **Cause:** Raised when a variable or function is referenced before it's defined.
- **Example:**
  ```python
  print(my_var)  
  # NameError: name 'my_var' is not defined
  ```

- **How to handle:** Ensure that all variables or functions are properly defined before using them.

---

### **11. `StopIteration`:**
- **Cause:** Raised to indicate the end of an iterator's sequence, typically when used in loops like `for` or `while`.
- **Example:**
  ```python
  my_iter = iter([1, 2, 3])
  next(my_iter)
  next(my_iter)
  next(my_iter)
  next(my_iter)  
  # StopIteration
  ```

- **How to handle:** This exception is mostly handled internally by Python in loops, so users rarely encounter it unless using `next()` explicitly.

---

### **12. `RuntimeError`:**
- **Cause:** Raised when an error occurs that doesn't fall into any specific category. This is a generic exception that covers errors that happen at runtime but are not necessarily tied to a particular issue like an index or value error.
- **Example:**
  ```python
  raise RuntimeError("An unknown error occurred")
  ```

- **How to handle:** You should handle the specific cause of the error if known, otherwise catch the exception and log the details for further investigation.

---

### **13. `OverflowError`:**
- **Cause:** Raised when a calculation exceeds the maximum limit for a numeric type.
- **Example:**
  ```python
  import math
  math.exp(1000)  
  # OverflowError: math range error
  ```

- **How to handle:** Avoid operations that result in numbers too large for Python to handle, or catch the error and deal with it appropriately.

---

### **14. `IndentationError`:**
- **Cause:** Raised when there is an incorrect indentation in Python code.
- **Example:**
  ```python
  def my_function():
  print("Hello")  
  # IndentationError: expected an indented block
  ```

- **How to handle:** Ensure that your code is indented correctly according to Python's requirements.

---

### **15. `MemoryError`:**
- **Cause:** Raised when an operation runs out of memory.
- **Example:**
  ```python
  my_list = [1] * (10**10)  # Trying to create a list too large for memory
  # MemoryError
  ```

- **How to handle:** Optimize your code to use less memory or use generators instead of lists.

---

### **16. `AssertionError`:**
- **Cause:** Raised when an `assert` statement fails. Assertions are used for debugging and testing, and if the condition in an `assert` statement is false, Python raises this error.
- **Example:**
  ```python
  assert 2 + 2 == 5, "Math is wrong!"  
  # AssertionError: Math is wrong!
  ```

- **How to handle:** Ensure that the assertion condition is correct or catch the `AssertionError` for debugging purposes.


"""