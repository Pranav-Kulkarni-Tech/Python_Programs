fruits={'apple':'red','banana':"yellow",'mango':'green'}
print(fruits)

name={'pranav','arjun','viraj'}
info=dict.fromkeys(name,'boy')
print(info)

for fr in fruits.keys():
    print(fr)
print("thse are values")
for va in fruits.values():
    print(va)

print("items use")
for ele in fruits.items():
    print(ele)

print("using key value ites without bracket")
for key,value in fruits.items():
    print(key,value)

print("finding apple color")
apple_color=fruits['apple']
print(apple_color)


fruits['apple']='black'
print(fruits)

fruits['greps']='green'
print(fruits)

print(fruits.get('mango'))

new_dict= {'age':12, 'year':2023}
fruits.update(new_dict)
print(fruits)
print('apple'in fruits)
print('chips'in fruits)

key,value=fruits.popitem()
print(key,value)
print(fruits)


