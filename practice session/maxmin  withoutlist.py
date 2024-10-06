#maxmimux number in list without any Method
l=[1,22,111,332,432,8]
maximum=l[0]
minimum=l[0]
for num in l:
    if num > maximum:
        maximum=num

       

    if num <minimum:
        minimum=num

print(maximum)
print(minimum)




