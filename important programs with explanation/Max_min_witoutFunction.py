#maxmimux number in list without any Method
l=[1,22,111,332,432,8]
maximum=l[0]
minimum=l[0]
for num in l:
    if num > maximum:
        maximum=num

       

    if num <minimum:
        minimum=num

print(maximum)
print(minimum)

"""
Initialization:

We start with the list l = [1, 22, 111, 332, 432, 8].
We create a variable maximum and assign it the value of the first element in the list, l[0], which is 1. This is our initial guess for the maximum.
Looping and Checking:

The for loop begins iterating through each element (num) in the list.

Inside the loop, we have the first if statement that checks if the current element (num) is greater than the current maximum:

if num > maximum:
Let's consider each element in the list:

Iteration 1: num is 1, which is not greater than the current maximum (1). So, the if condition is False, and maximum remains unchanged at 1.
Iteration 2: num becomes 22. Since 22 is greater than the current maximum (1), the if condition becomes True.
Inside the if block, maximum is updated to the value of num (which is 22). Now, maximum reflects the largest number encountered so far.
Iteration 3: num becomes 111. Here, 111 is greater than the current maximum (22), so the if condition is True again.
maximum is updated to 111, reflecting the new largest number.
Iteration 4: num becomes 332. Similar to the previous case, 332 is greater than 111, so maximum is updated to 332.
Iteration 5: num becomes 432. This is the largest element in the list. Since 432 is greater than the current maximum (332), the if condition is True.
maximum is updated to 432, which becomes the final maximum value.
Iteration 6: num becomes 8, which is not greater than the current maximum (432). So, the if condition is False, and maximum remains unchanged at 432.







The for loop starts iterating through each element (num) in the list.

Inside the loop, we have the second if statement that checks if the current element (num) is less than the current minimum:

if num < minimum:
Let's consider each element in the list:

Iteration 1: num is 1, which is equal to the current minimum (1). So, the if condition is False, and minimum remains unchanged at 1.
Iteration 2: num becomes 22. Since 22 is not less than the current minimum (1), the if condition is False, and minimum remains unchanged.
Iteration 3: num becomes 111. Similar to the previous case, 111 is not less than 1, so minimum stays at 1.
Iteration 4: num becomes 332. Here, 332 is not less than 1. The if condition is False, and minimum remains unchanged.
Iteration 5: num becomes 432. This doesn't affect minimum as it's not less than 1.
Iteration 6: num becomes 8. This is the smallest element in the list. Since 8 is less than the current minimum (1), the if condition becomes True.
Inside the if block, minimum is updated to the value of num (which is 8). Now, minimum reflects the smallest number encountered so far.
Key Points:

The if statement ensures that only elements smaller than the current minimum are allowed to update it.
This approach efficiently finds the minimum value by iterating through the list and updating minimum only when a smaller element is encountered.
At the end of the loop, minimum will always hold the smallest element in the list.

"""






