
#sorting dictionarey key or we can also sort values
dict1={'raj':555,'arjun':781,'pranav':100,'rucha':199}

s=sorted(dict1.items(),key=lambda x:x[0] )# here 0 is key and 1 is value
print(s)