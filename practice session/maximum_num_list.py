list1=[44,3,22,445,32]

maximum=list1[0]
minimum=list1[0]

for num in list1:
    if num>maximum:
        maximum=num

print(maximum)


for num in list1:
    if num<minimum:
        minimum=num
print(minimum)