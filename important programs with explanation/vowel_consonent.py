string=input("Enter a string")

count_vowels=0
count_consonent=0

vowels='aeiou'

for i in vowels:
    if i in string:
        count_vowels +=1

    else:
        count_consonent +=1


print("number of vowels is",count_vowels)

print("number of consonent",count_consonent)


