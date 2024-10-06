def leap(year):
    return (year%4==0 and year%100!=0) or (year%400==0)


year=int(input("enter a year"))
if leap(year):
    print(f"{year} is leap")
else:
    print(f"{year} is not leap")        
        

"""
The code you provided correctly identifies 2000 as a leap year, and here’s why:

### Understanding the Leap Year Logic in Your Code

```python
def leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter a year: "))
if leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

### Explanation of the Conditions

1. **Condition: `(year % 4 == 0 and year % 100 != 0)`**
   - This checks if the year is divisible by 4 **and** not divisible by 100. 
   - For example:
     - **Year 1996**: 
       - \(1996 \mod 4 = 0\) (divisible by 4) 
       - \(1996 \mod 100 = 96\) (not divisible by 100) 
       - **Result**: Leap year.

     - **Year 1900**:
       - \(1900 \mod 4 = 0\) (divisible by 4) 
       - \(1900 \mod 100 = 0\) (divisible by 100) 
       - **Result**: Not a leap year (fails this condition).

2. **Condition: `(year % 400 == 0)`**
   - This checks if the year is divisible by 400.
   - If a year is divisible by 400, it is a leap year, regardless of whether it is also divisible by 100.
   - For example:
     - **Year 2000**:
       - \(2000 \mod 4 = 0\) (divisible by 4)
       - \(2000 \mod 100 = 0\) (divisible by 100)
       - \(2000 \mod 400 = 0\) (divisible by 400)
       - **Result**: Leap year.

### Putting It All Together

- The function `leap(year)` returns `True` if either of the conditions is satisfied:
  - A year is a leap year if:
    - It is divisible by 4 **and** **not** divisible by 100 **OR**
    - It is divisible by 400.

So, for the year **2000**:
- It is divisible by **4**: \(2000 \mod 4 = 0\)
- It is divisible by **100**: \(2000 \mod 100 = 0\)
- It is also divisible by **400**: \(2000 \mod 400 = 0\)

### Conclusion
Since the year **2000** meets the condition of being divisible by **400**, the function correctly identifies it as a leap year, even though it is also divisible by **100**. The key point is that the rule for being divisible by **400** takes precedence over being divisible by **100**. 

### Example Outputs
- For the input **2000**, the output will be: 
  ```
  2000 is a leap year.
  ```
- For the input **1900**, the output will be:
  ```
  1900 is not a leap year.
  ```
This implementation is correct and accurately reflects the rules for leap years!


Sure! Let’s break down the three conditions step by step to clarify how they determine if a year is a leap year.

### Leap Year Rules

In the Gregorian calendar, the rules for determining if a year is a leap year are:

1. A year is a leap year if it is **divisible by 4**.
2. However, if a year is **divisible by 100**, it is **not** a leap year **unless** it is also **divisible by 400**.
   - This means that:
     - Years like 1900 are **not** leap years (divisible by 100 but **not** by 400).
     - Years like 2000 are leap years (divisible by both 100 and 400).

### Breaking Down the Conditions

Let’s look at the specific conditions you mentioned:

1. **Condition: `year % 4 == 0`**
   - **What it checks**: If the year is divisible by 4.
   - **Reason**: Any year divisible by 4 has a potential to be a leap year. For example, 2024 % 4 equals 0, meaning 2024 is a candidate for being a leap year.

2. **Condition: `and year % 100 != 0`**
   - **What it checks**: If the year is **not** divisible by 100.
   - **Reason**: Although a year might be divisible by 4, it cannot be a leap year if it is also divisible by 100 unless it meets the next condition. 
   - **Example**: For the year 1900:
     - 1900 % 4 = 0 (divisible by 4, so it could be a leap year).
     - 1900 % 100 = 0 (divisible by 100).
     - Since 1900 is divisible by 100, it cannot be a leap year, which we verify with the next condition.

3. **Condition: `or year % 400 == 0`**
   - **What it checks**: If the year is divisible by 400.
   - **Reason**: This condition serves as an exception to the previous rule about divisibility by 100. If a year is divisible by 400, it is indeed a leap year, regardless of the previous conditions.
   - **Example**: For the year 2000:
     - 2000 % 4 = 0 (divisible by 4).
     - 2000 % 100 = 0 (divisible by 100).
     - 2000 % 400 = 0 (divisible by 400).
     - Since it meets the condition of being divisible by 400, 2000 is a leap year.

### Putting It All Together

Let’s analyze how these conditions work together in your original code:

```python
return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```

1. **Check if the year is a leap year**:
   - **First part**: `(year % 4 == 0 and year % 100 != 0)`
     - This checks if the year is divisible by 4 **and** not divisible by 100. If both conditions are true, the year is a leap year.
   - **Second part**: `(year % 400 == 0)`
     - This checks if the year is divisible by 400. If this condition is true, the year is also a leap year.

2. **Result**:
   - If either of these two conditions is true, the function returns `True`, indicating it is a leap year.
   - If neither condition is true, it returns `False`, indicating it is **not** a leap year.

### Summary

- A year is a leap year if:
  - It is divisible by 4 **and** **not** divisible by 100.
  - **OR** it is divisible by 400.
  
This logic ensures that the exceptions to the rules (like years divisible by 100) are handled appropriately, making it a robust method for determining leap years.
"""