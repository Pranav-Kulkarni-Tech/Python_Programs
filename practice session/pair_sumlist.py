#pair in sum of list +

list=[1,2,3,4,1,2,1,0]
n=len(list)
k=2
for i in range(n):
    for j in range(i+1,n):
        if list[i]+list[j]==k:
            print(list[i],"+" ,list[j],"=2")
