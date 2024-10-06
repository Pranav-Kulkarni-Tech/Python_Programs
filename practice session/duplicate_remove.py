#remove  duplicate element in list

def remove_duplicate(my_list):
    unique_list=[]
    for item in my_list:
        if item not in unique_list:
           unique_list.append(item)
    return unique_list
        
my_list=[1,2,1,1,2,3,3,4,4]
unique_list=remove_duplicate(my_list)
print("dupliacte list is",unique_list)