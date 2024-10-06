unsorted_list=[3,1,4,222,3,444,52,23,2,2,33]


for i in range(len(unsorted_list)):
    for j in range(i+1,len(unsorted_list)):
        
        if unsorted_list[i]> unsorted_list[j]:
            unsorted_list[i],unsorted_list[j]=unsorted_list[j],unsorted_list[i]
            

print("unsorted_list is \n",unsorted_list)


                   