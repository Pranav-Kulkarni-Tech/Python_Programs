s='Pranav Govind Kulkarni'
p=s.split(' ')
print(p)

p=p[::-1]
print(p)

p=' '.join(p)
print(p)

"""
Original String:

n = 'pranav govind kulkani': This is your original string.
print(n): This prints the original string.
Splitting the String:

names = n.split(' '): This splits the string n into a list of words based on spaces. The list will be ['pranav', 'govind', 'kulkani'].
print(names): This prints the list of words.
Reversing the List:

names = names[::-1]: This reverses the list of words. The reversed list will be ['kulkani', 'govind', 'pranav'].
print(names): This prints the reversed list.
Joining the Words:

names = ' '.join(names): This joins the reversed list of words back into a single string with spaces between them. The result will be 'kulkani govind pranav'.
print(names): This prints the final reversed string.
"""