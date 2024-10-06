#remove puctuations

str1='pranav @ you are  best **() #  its golden $ chance'
s=''
for i in str1:
    if ((i>='A' and i<='Z') | (i>='a' and i<='z') | (i==' ')):
        s=s+i
print(s) 