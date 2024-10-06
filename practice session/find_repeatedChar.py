#find repeated charcter in string without having on 2 complexity
s='pranavgovindkukarnippgaa'
ch={}
for i in s:
    if i in ch:
        ch[i]=ch[i]+1
    else:
        ch[i]=1
print(ch)

max_char=max(ch,key=ch.get)
print(max_char)
