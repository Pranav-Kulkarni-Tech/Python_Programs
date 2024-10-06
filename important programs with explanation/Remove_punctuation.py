st1=' pranav @ 90i am8best '
s=''

for i in st1:
    if ((i>='A' and i<='Z') | (i>='a' and i<='z') | (i==' ')):
        s=s+i
print(s)