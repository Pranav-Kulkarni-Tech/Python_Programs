#Basic Usage: Write a Python program to combine two lists into a list of tuples using the zip() function.
li1=[2,3,4]
li2=[7,8,9]

list3=zip(li1,li2)
print(list(list3))


unzip=[(1,5),(2,4),(3,9)]
list1,list2=zip(*unzip)
print(list1)
print(list2)


