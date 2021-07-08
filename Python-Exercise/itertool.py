from itertools import *

# Q1: Use itertools to create groups of similar items of a given list.
"""
Input:
names = ['Thomas Brown', 'Tom Smith', 'Jane Brown', 'John Smith']
Output:
[ ['Thomas Brown', 'Jane Brown'], ['Tom Smith', 'John Smith'] ]
"""
names = ['Thomas Brown', 'Tom Smith', 'Jane Brown', 'John Smith']

# Split each names into many subname strings
splitLst = [x.split(' ') for x in names]

# Get unique sub-names from flatten list 
subNames = list(set(chain.from_iterable(splitLst)))

# Get list of names in which has common unique subname
commonNames = [[list(group)[0] for key, group in groupby(names, lambda name: sub in name) if key] for sub in subNames]

# Get list common name which has at least 2 names
print("============== Q1: ==============")
print(list(filter(lambda x: len(x)>1, commonNames)))



#Q2: Use itertools to combine two list into a new list
"""
Input:
list1 = [ ['We', 'are'], 'Novobi']
list2 = [ 'We', ['are', 'Odoo'] ]
Output:
['We', 'are', 'Novobi', 'We', 'are', 'Odoo']
"""

list1 = [ ['We', 'are'], 'Novobi']
list2 = [ 'We', ['are', 'Odoo'] ]
q2 = list(chain.from_iterable(map(lambda x: [x] if isinstance(x,str) else x, list1 + list2)))

print("============== Q2: ==============")
print(q2)



# Q3: Generate unique combinations
"""
Input:
list = ['Red', 'Green', 'Blue']
Output:
list = ['Red and Green', 'Red and Blue', 'Green and Blue']
"""

lst = ['Red', 'Green', 'Blue']
q3 = list(map(lambda x: x[0] + ' and ' + x[1], combinations(lst, 2)))

print("============== Q3: ==============")
print(q3)