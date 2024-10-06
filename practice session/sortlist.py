unsorted_list=[99,23,12,55,3,66]

for i in range(len(unsorted_list)):
    for j in range(i+1,len(unsorted_list)):
        if unsorted_list[i]>unsorted_list[j]:
            unsorted_list[i],unsorted_list[j]=unsorted_list[j],unsorted_list[i]
print(unsorted_list)
