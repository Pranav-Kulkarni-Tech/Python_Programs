sample={'name':'pranav',
        'age':52,
        'country':'India'
        }

copy_dict=sample.copy()

print("copy dictinary", copy_dict)

key=sample.keys()
print("keys",key)

value=sample.values()
print("values", value)

print("keys without bracket")
for key in sample.keys():
    print(key)

print("values without bracket")
for value in sample.values():
    print(value)

print("keys, values without bracket through items")
for key,value in sample.items():
    print(f"{key}:{value}")

print("key values with brackets")
item=sample.items()
print(item)

updated_dict={'graduation':'BCA',
        'Year':2011,
        'marks':62}

print("update")
sample.update(updated_dict)
print(sample)

va_year=sample.get("year")
print("year is",va_year)

age_value=sample['age']
print(age_value)

name=sample['name']
print(name)


student={'yash':22, 'ram':11, 'arjun':12}
merge=sample| student
print(merge)


cube={x:x**3 for x in range(2,9) }
print(cube)
