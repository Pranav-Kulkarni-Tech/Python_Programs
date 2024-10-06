def vowels(string):
    count_vowels=0
    count_consonent=0

    vowels='aeiou'
    string=string.lower()
    for char in string:
        if char.isalpha:
            if char in vowels:
                count_vowels+=1

            else:
                count_consonent+=1

    print("consonent",count_consonent)
    print("vowels",count_vowels)

string=input("enter a string")

vowels(string)

