name=[1,1,1,4,5,4,5]
n=[]
for i in name:
    if i not in n:
        n.append(i)
print(n)