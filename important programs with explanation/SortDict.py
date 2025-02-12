dictionary={'pranav':29, 'ram':11,'Arjun':56}

s=sorted(dictionary.items(),key=lambda x:x[1])# [0] is key and [1] is value
print(s)

"""
dictionary = {'pranav': 29, 'ram': 11, 'Arjun': 56}:

This creates a dictionary named dictionary with keys ('pranav', 'ram', 'Arjun') and their corresponding values (29, 11, 56).
dictionary.items():

The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
For dictionary, dictionary.items() will return [('pranav', 29), ('ram', 11), ('Arjun', 56)].
sorted(dictionary.items(), key=lambda x: x[1]):

The sorted() function is used to sort the items of the dictionary.
sorted() takes two main arguments: the iterable to be sorted (in this case, dictionary.items()) and a key function that determines the sorting criteria.
lambda x: x[1] is a lambda function used as the key for sorting. It takes each item (which is a tuple like ('pranav', 29)) and returns x[1], which is the second element of the tuple—the value of the dictionary.
As a result, the dictionary is sorted by its values in ascending order.
print(s):

This prints the sorted list of tuples.
[('ram', 11), ('pranav', 29), ('Arjun', 56)]


"""