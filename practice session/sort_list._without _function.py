list1=[44,33,2,444,2122,22,11]

l=len(list1)

for i in range(l):
    for j in range(i+1,l):

        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]



print(list1)