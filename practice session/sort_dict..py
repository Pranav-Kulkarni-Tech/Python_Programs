dict1={'raj':55,'arjun':78,'pranav':100,'rucha':99}

d=sorted(dict1.keys)
dict2={}
for i in d:
    dict2[i]=dict1[i]
print(dict2)
