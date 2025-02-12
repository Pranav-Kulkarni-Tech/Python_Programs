list1=[3,66,33,2,55,31]
maximum=list1[0]
minimum=list1[0]
for num in list1:
    if num>maximum:
        maximum=num

    if num<minimum:
        minimum=num

print(minimum)
print(maximum)