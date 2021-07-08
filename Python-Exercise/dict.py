# Q1: Use “zip” function to map two lists into a dictionary
############################################################################
""" 
Input:
Keys = ['Key 1', 'Key 2', 'Key 3']
Values = ['Value 1', 'Value 2', 'Value 3']
Output:
Dict = {'Key 1': 'Value 1', 'Key 2': 'Value 2', 'Key 3': 'Value 3'}
"""

keys = ['Key 1', 'Key 2', 'Key 3']
values = ['Value 1', 'Value 2', 'Value 3']
dict1 = dict(zip(keys, values))

print("============== Q1: ==============")
print(dict1)



# Q2: Check multiple keys exists in a dictionary
############################################################################
"""
Input:
Dict = {'Key 1': 'Value 1', 'Key 2': 'Value 2', 'Key 3': 'Value 3'}
list1 = ['Key 1', 'Key 5']
list2 = ['Key 2', 'Key 3']
Output:
Check list1 -> False
Check list2 -> True
"""

dict2 = {'Key 1': 'Value 1', 'Key 2': 'Value 2', 'Key 3': 'Value 3'}
keyLst1 = ['Key 1', 'Key 5']
keyLst2 = ['Key 2', 'Key 3']

print("============== Q2: ==============")

# Way 1:
def isKeysExist(dict, keys):
    for k in keys:
        if k not in dict.keys():
            return False
    
    return True
# print(isKeysExist(dict2, keyLst1))
# print(isKeysExist(dict2, keyLst2))

# Way 2:
print(set(keyLst1) <= dict2.keys())
print(set(keyLst2) <= dict2.keys())

# Way 3:
# print(set(keyLst1).issubset(dict2.keys()))
# print(set(keyLst2).issubset(dict2.keys()))



# Q3: Remove a key from a dictionary
############################################################################
"""
Input:
Dict = {'Key 1': 'Value 1', 'Key 2': 'Value 2'}
Key = 'Key 1'
Output:
Dict = {'Key 2': 'Value 2'}
"""

dict3 = {'Key 1': 'Value 1', 'Key 2': 'Value 2'}
key = 'Key 1'

print("============== Q3: ==============")
if key in dict3.keys():
    dict3.pop(key)
else:
    print("Key not found!")
    
print(dict3)


# Q4: Iterate over dictionaries using for loops.
############################################################################
"""
Input:
Dict = {'Key 1': 'Value 1', 'Key 2': 'Value 2'}
Output:
Key 1 corresponds to Value 1
Key 2 corresponds to Value 2
"""

dict4 = {'Key 1': 'Value 1', 'Key 2': 'Value 2'}
print("============== Q4: ==============")
[print(key + " corresponds to " + val) for (key, val) in dict4.items()]



#Q5: Count number of items in a dictionary value that is a list by using sum and map
############################################################################
"""
Input:
Dict = {'Key 1': ['Value 1', 'Value 2'], 'Key 2': ['Value 3', 'Value 4', 'Value 5']}
Output: 5
"""

dict5 = {'Key 1': ['Value 1', 'Value 2'], 'Key 2': ['Value 3', 'Value 4', 'Value 5']}
numItems = sum(map(lambda x: len(x), dict5.values()))

print("============== Q5: ==============")
print(numItems)



# Q6: Store a given dictionary in a json file
############################################################################
"""
Input:
Dict = {'Key 1': ['Value 1', 'Value 2'], 'Key 2': ['Value 3', 'Value 4', 'Value 5']}
Output:
JSON file
"""

import json

dict6 = {'Key 1': ['Value 1', 'Value 2'], 'Key 2': ['Value 3', 'Value 4', 'Value 5']}

print("============== Q6: ==============")
# Serializing json   
json_obj = json.dumps(dict6)
print(json_obj)

# Writting to q6.json
with open("q6.json", "w") as outfile: 
    json.dump(dict6, outfile)

