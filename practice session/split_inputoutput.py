"""
input= ' sky is blue
output= blue is  sky 
"""
s='  sky is   blue'
print(s)
a=s.split(' ')
a=a[ :  :-1]
a=' '.join(a)
print(a)
