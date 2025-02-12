#remove duplicate elements in list  

l=[1,2,1,1,2,3,4,4,4,5,5,6]
li=[]
for i in l:
    if i not in li:
        li.append(i)
print(li)





