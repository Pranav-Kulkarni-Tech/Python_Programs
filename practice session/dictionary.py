di={'pranav':29, 'arjun':11, 'raj':16}
new_dict={'abhay':33}
di.update(new_dict)
print(di)


acess_value=di['pranav']
print(acess_value)

for d in di.items():
    print(d)

for k in di.keys():
    print(k) 

keys={'pg','rk','sk'}
values='unkonown'

dictionary=dict.fromkeys(keys,values)
print(dictionary)