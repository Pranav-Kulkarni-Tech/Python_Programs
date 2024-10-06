dic={'pg':24, 'sg':23,'rpg':222}
d=sorted(dic.items(),key=lambda x:x[0])
print(d)

sort_values=sorted(dic.items(),key=lambda x:x[1])
print(sort_values)


dictionary={'pune':29, 'mumbai':11, 'india':100}
sorting_values=sorted(dictionary.items(),key=lambda x:x[1])
print(sorting_values)

sorting_keys=sorted(dictionary.items(),key=lambda x:x[0])
print(sorting_keys)