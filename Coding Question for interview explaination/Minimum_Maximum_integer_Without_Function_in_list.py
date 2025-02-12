# Find the largest and smallest numbers in a list of integers without function

list1=[44,3,22,445,32]

maximum=list1[0]
minimum=list1[0]

for num in list1:
    if num>maximum:
        maximum=num

print(maximum)


for num in list1:
    if num<minimum:
        minimum=num
print(minimum)


"""
First, we assume the first element, 44, is both the maximum and minimum. Then, we iterate over the list. When we compare 44 (the current maximum) with 3, we find that 3 is not greater than 44, so the maximum remains 44. Next, we compare 44 with 22. Since 22 is smaller, the maximum remains 44. When we compare 44 with 445, 445 is greater, so the maximum becomes 445. Finally, comparing 445 with 32, 32 is not greater than 445, so the maximum remains 445.

For the minimum, we start with 44 as the assumed minimum. Comparing 44 with 3, 3 is smaller, so the minimum is updated to 3. The next comparisons of 22, 445, and 32 do not change the minimum, as none are smaller than 3. So, the final minimum is 3, and the maximum is 445.
"""