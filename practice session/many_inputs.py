# Giving many input using single time

x=list(map(int,input("enter a multiple numbers").split()))
print(x)

p=[int(x) for x in input("enter a values of p").split()]
print("enter a values of p",p)

"""
x=list(map(int,input("enter a multiple numbers").split()))
print(x)

1. input("enter multiple numbers"):
Purpose: This function prompts the user to enter a series of numbers.
How it Works:
The input() function waits for the user to type something and press Enter.
The string "enter multiple numbers" is displayed as a prompt message to the user.
The input provided by the user is read as a single string.
For example, if the user types 1 2 3 4 5 and presses Enter, the result of input() will be the string "1 2 3 4 5".
2. .split():
Purpose: This method splits the input string into a list of substrings based on whitespace (space) by default.
How it Works:
The split() method breaks the string "1 2 3 4 5" into individual components (substrings) wherever there's a space.
It returns a list of strings: ['1', '2', '3', '4', '5'].
3. map(int, ...):
Purpose: The map() function applies the int function to each element of the list produced by split().
How it Works:
map() is used to transform each string in the list ['1', '2', '3', '4', '5'] into an integer.
int is the function that converts a string representation of a number into an actual integer.
The result of map(int, ...) is an iterable map object that contains integers: [1, 2, 3, 4, 5].
4. list(...):
Purpose: The list() function converts the map object into a list of integers.
How it Works:
The map object itself is not a list, so we convert it into a list explicitly.
The final result is the list [1, 2, 3, 4, 5].
5. x = ...:
Purpose: The result of the entire expression is assigned to the variable x.
How it Works:
After processing the input, x will hold the list [1, 2, 3, 4, 5].
6. print(x):
Purpose: This line prints the list x to the console.
How it Works:
When print(x) is executed, it outputs the contents of the list x.
For our example, it will print [1, 2, 3, 4, 5].
Summary:
The entire code reads multiple numbers from the user as a single string, splits that string into individual substrings, converts those substrings into integers, stores them in a list, and finally prints the list.
Example Execution:

If the user inputs: 10 20 30 40 50
The output will be: [10, 20, 30, 40, 50]
"""