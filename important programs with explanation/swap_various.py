#swap first and last element of string

s='hello'
s=s[-1] + s[1:-1] +s[0]
print(s)



#swap first and  last element  list

p=[15,22,33,44,61]
p[0],p[4]=p[4],p[0]
print(p)


#swap numbers using arithemetic operations

a=5
b=10
print("a",a)
print("b",b)

a=a+b #a=15

b=a-b #b=15-10=5 b=5

a=a-b #a=15-5=10 a=10

print("a",a)
print("b",b)





# swap  without using temparary variable

x=2
y=3
print("x",x)
print("y",y)
x,y=y,x
print("x",x)
print("y",y)




#swap using temp

p=1
q=2
print("p",p)
print("q",q)

temp=p
p=q
q=temp

print("p",p)
print("q",q)



"""
Here is a breakdown of each program and the logic behind them:

### 1. **Swap the First and Last Elements of a String**

```python
s = 'hello'
s = s[-1] + s[1:-1] + s[0]
print(s)
```

- **Explanation**: 
  - `s[-1]`: This accesses the last character of the string (`'o'`).
  - `s[1:-1]`: This accesses all characters except the first and last (`'ell'`).
  - `s[0]`: This accesses the first character (`'h'`).
  - The new string is formed by concatenating the last character, middle part, and first character.
- **Output**: `'oellh'`

### 2. **Swap the First and Last Elements of a List**

```python
p = [15, 22, 33, 44, 61]
p[0], p[4] = p[4], p[0]
print(p)
```

- **Explanation**:
  - `p[0], p[4] = p[4], p[0]`: This swaps the first (`15`) and last (`61`) elements of the list.
- **Output**: `[61, 22, 33, 44, 15]`

### 3. **Swap Numbers Using Arithmetic Operations**

```python
a = 5
b = 10
print("a", a)
print("b", b)

a = a + b  # a = 15
b = a - b  # b = 15 - 10 = 5
a = a - b  # a = 15 - 5 = 10

print("a", a)
print("b", b)
```

- **Explanation**:
  - `a = a + b`: Adds `a` and `b` and stores the result in `a`.
  - `b = a - b`: Subtracts `b` from the new `a`, leaving the original value of `a` in `b`.
  - `a = a - b`: Subtracts the new `b` from `a`, restoring the original value of `b` in `a`.
- **Output**: `a = 10`, `b = 5`

### 4. **Swap Two Numbers Without Using a Temporary Variable**

```python
x = 2
y = 3
print("x", x)
print("y", y)
x, y = y, x
print("x", x)
print("y", y)
```

- **Explanation**: 
  - `x, y = y, x`: This uses Python's tuple unpacking feature to swap the values of `x` and `y` without the need for a temporary variable.
- **Output**: `x = 3`, `y = 2`

### 5. **Swap Two Numbers Using a Temporary Variable**

```python
p = 1
q = 2
print("p", p)
print("q", q)

temp = p
p = q
q = temp

print("p", p)
print("q", q)
```

- **Explanation**:
  - A temporary variable `temp` stores the value of `p`.
  - The value of `q` is assigned to `p`.
  - Finally, the value stored in `temp` (original `p`) is assigned to `q`.
- **Output**: `p = 2`, `q = 1`

These programs demonstrate different techniques to swap values in strings, lists, and variables.
"""