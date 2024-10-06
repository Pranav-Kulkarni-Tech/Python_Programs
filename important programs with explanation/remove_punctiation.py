"""
Remove Punctiontion from string
"""


str1=' My  4 29 @ name ,. is $ % Pranav'

s=''

for i in str1:
    if ((i>='A' and i<='z') | (i>='a' and i<='z') | (i==' ')):
        s=s+i

print(s)