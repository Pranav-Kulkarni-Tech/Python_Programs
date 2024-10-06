#find sum of pair of element of list is 4

l=[1,2,34,5,1,2,3,1,2,3,4,5,6,7,32,2,1,0]
n=len(l)
k=4
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            print(f"{l[i]} + {l[j]} == {k}")

