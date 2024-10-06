list1=[189,67,55,45,222,33,187,65]

l=len(list1)
for i in range(l):
    for j in range(i+1,l):

        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]

print(list1)
