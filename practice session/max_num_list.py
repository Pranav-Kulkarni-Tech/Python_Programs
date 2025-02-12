list1=[23,433,1,55,65,666,76,78,98,34,55]
maximum=list1[0]
minimum=list1[0]

for num in list1:
    if num>maximum:
        maximum=num

    if num<minimum:
        minimum=num

print(maximum)
print(minimum)

print(max(list1))
print(min(list1))