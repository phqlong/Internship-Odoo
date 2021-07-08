# Q1: Concatenate two lists index-wise by using list comprehension
############################################################################
"""
Input:
list1 = ['W, 'a', 'Novo']
list2 = ['e', 're', bi']
Output:
List = ['We', 'are', 'Novobi']
"""

list1 = ['W', 'a', 'Novo']
list2 = ['e', 're', 'bi']
q1 = [s1+s2 for s1, s2 in zip(list1, list2)] 
print("============== Q1: ==============")
print(q1)



# Q2: Concatenate two lists in the following order
############################################################################
"""
Input:
list1 = ['Hello ', ' take ']
list2 = ['Dear', 'Sir']
Output:
List = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

list1 = ['Hello ', ' take ']
list2 = ['Dear', 'Sir']
q2 = [s1+s2 for s1 in list1 for s2 in list2 ] 
print("============== Q2: ==============")
print(q2)



# Q3: Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order by using zip function
############################################################################
"""
Input:
list1 = ['10', '20', '30']
list2 = ['100', '200', '300']
Output:
10 100
20 200
30 300
"""
list1 = ['10', '20', '30']
list2 = ['100', '200', '300']
print("============== Q3: ==============")
[print(s1 + ' ' + s2) for s1, s2 in zip(list1, list2[::-1])] 



# Q4: Remove empty strings from the list of strings by using filter function
############################################################################
"""
Input:
List = ['10', '20', '30', '', '40']
Output:
List = ['10', '20', '30', '40']
"""
lst = ['10', '20', '30', '', '40']
q4 = list(filter(lambda x: x != '', lst))
print("============== Q4: ==============")
print(q4)



# Q5: Remove all occurrence of 20 from the list by using list comprehension
############################################################################
"""
Input:
List = ['10', '20', '30', '40', '20', '50']
Output:
List = ['10', '30', '40', '50']
"""
lst = ['10', '20', '30', '40', '20', '50']
q5 = [x for x in lst if x != '20']
print("============== Q5: ==============")
print(q5)



# Q6: Sort a list of dictionaries using Lambda.
############################################################################
"""
Input:
List = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Output:
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color':
'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
q6 = sorted(lst, reverse=True, key=lambda x: int(x['model']))
print("============== Q6: ==============")
print(q6)