# sort list without using any function

li=[122,81,4,22,3,21,12]

for i in range(len(li)):
    for j in range(i+1,len(li)):

        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print(li)

""""
0 index element compare with all index then 1 index compare with all index the index 2 compare with all remaining index

In first iteration


i is  index 0
j is always iterates  the every element index is ths list 
i compares j. index of i is always 0 compares every element  in list 
if i>j then it replace i and j value

in second iteration

when i  comapres last index then i index becomes 1
then index 1 compares all index till end and replace i=j if i>j 

in third iteration

i index  become 2 and it compare till last index 
 and so gon  repeate this step

 
 

Detailed Explanation
Initialization:

The list li is initialized with the values [122, 81, 4, 22, 3, 21, 12].
Outer Loop (for i in range(len(li))):

The outer loop iterates over each index i in the list li. The range(len(li)) generates a sequence of numbers from 0 to the length of the list minus 1.
The variable i represents the index of the current element in the list li that will be compared with the rest of the elements.
Inner Loop (for j in range(i + 1, len(li))):

The inner loop iterates over the indices j, starting from i + 1 to the last index of the list.
This ensures that every element following the element at index i is compared to the element at index i.
Comparison and Swapping (if li[i] > li[j]):

Inside the inner loop, the code checks if the element at index i is greater than the element at index j.
If li[i] is greater than li[j], it means the elements are out of order, and they need to be swapped.
The swapping is done using the tuple unpacking method: li[i], li[j] = li[j], li[i].
Process Overview:

First Iteration (i = 0):

j iterates from 1 to 6 (the length of the list minus one).
The element at index 0 (li[0] = 122) is compared with each of the elements at indices 1 to 6.
If 122 is greater than any of these elements, it is swapped with that element.
Second Iteration (i = 1):

j iterates from 2 to 6.
The element at index 1 (li[1]) is compared with each of the elements at indices 2 to 6.
If the element at index 1 is greater than any of these elements, it is swapped with that element.
Subsequent Iterations (i = 2, 3, ...):

The process continues similarly, with i increasing each time and j iterating from i + 1 to the end of the list.
Each element is compared with the elements that follow it, and swaps are made as necessary.
Completion:

The loops continue until all elements have been compared and placed in their correct positions.
After all iterations, the list li is sorted in ascending order.
Final Output:

The final sorted list is printed: [3, 4, 12, 21, 22, 81, 122].
Example Walkthrough
Let's walk through the sorting process with the initial list [122, 81, 4, 22, 3, 21, 12]:

First Iteration (i = 0):

li[0] (122) is compared with li[1] (81). Since 122 > 81, they are swapped.
List after the swap: [81, 122, 4, 22, 3, 21, 12]
li[0] (81) is compared with li[2] (4). Since 81 > 4, they are swapped.
List after the swap: [4, 122, 81, 22, 3, 21, 12]
li[0] (4) is compared with li[3] (22). No swap needed.
li[0] (4) is compared with li[4] (3). Since 4 > 3, they are swapped.
List after the swap: [3, 122, 81, 22, 4, 21, 12]
li[0] (3) is compared with li[5] (21). No swap needed.
li[0] (3) is compared with li[6] (12). No swap needed.
Second Iteration (i = 1):

li[1] (122) is compared with li[2] (81). Since 122 > 81, they are swapped.
List after the swap: [3, 81, 122, 22, 4, 21, 12]
li[1] (81) is compared with li[3] (22). Since 81 > 22, they are swapped.
List after the swap: [3, 22, 122, 81, 4, 21, 12]
li[1] (22) is compared with li[4] (4). Since 22 > 4, they are swapped.
List after the swap: [3, 4, 122, 81, 22, 21, 12]
li[1] (4) is compared with li[5] (21). No swap needed.
li[1] (4) is compared with li[6] (12). No swap needed.
Third Iteration (i = 2):

li[2] (122) is compared with li[3] (81). Since 122 > 81, they are swapped.
List after the swap: [3, 4, 81, 122, 22, 21, 12]
li[2] (81) is compared with li[4] (22). Since 81 > 22, they are swapped.
List after the swap: [3, 4, 22, 122, 81, 21, 12]
li[2] (22) is compared with li[5] (21). Since 22 > 21, they are swapped.
List after the swap: [3, 4, 21, 122, 81, 22, 12]
li[2] (21) is compared with li[6] (12). Since 21 > 12, they are swapped.
List after the swap: [3, 4, 12, 122, 81, 22, 21]
Fourth Iteration (i = 3):

li[3] (122) is compared with li[4] (81). Since 122 > 81, they are swapped.
List after the swap: [3, 4, 12, 81, 122, 22, 21]
li[3] (81) is compared with li[5] (22). Since 81 > 22, they are swapped.
List after the swap: [3, 4, 12, 22, 122, 81, 21]
li[3] (22) is compared with li[6] (21). Since 22 > 21, they are swapped.
List after the swap: [3, 4, 12, 21, 122, 81, 22]
Fifth Iteration (i = 4):

li[4] (122) is compared with li[5] (81). Since 122 > 81, they are swapped.
List after the swap: [3, 4, 12, 21, 81, 122, 22]
li[4] (81) is compared with li[6] (22). Since 81 > 22, they are swapped.
List after the swap: [3, 4, 12, 21, 22, 122, 81]
Sixth Iteration (i = 5):

li[5] (122) is compared with li[6] (81). Since 122 > 81, they are swapped.
List after the swap: [3, 4, 12, 21, 22, 81, 122]
Seventh Iteration (i = 6):

No comparisons needed, as there are no elements after index 6.
Final Output
The sorted list is: [3, 4, 12, 21, 22, 81, 122].

Summary of the Explanation
Outer loop (i) iterates through the entire list from the first to the last element.
Inner loop (j) iterates through the list starting from the element after i to the end of the list.
Each pair of elements (li[i] and li[j]) is compared, and if they are out of order (i.e., li[i] is greater than li[j]), they are swapped.
This process repeats, progressively sorting the list until it is in ascending order.

 
 
 """