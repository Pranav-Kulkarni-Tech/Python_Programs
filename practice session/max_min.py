list1=[51,33,22,55,3,11,34,15,66]

minimum=list1[0]
maximum=list1[0]

for i in list1:
    if i>maximum:
        maximum=i

    if i<minimum:
        minimum=i


print(minimum)
print(maximum)