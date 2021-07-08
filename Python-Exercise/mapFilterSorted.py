# Q1: Use “map” function for data type conversion
list1 = [10.8932, 12.434, 13.65656]
q1 = list(map(lambda x: int(x), list1))
print(q1)


# Q2: Use “filter” function to get positive numbers
list2 = [4, -3, 2]
q2 = list(filter(lambda x: x > 0, list2))
print(q2)


# Q3: Use “sorted” function to reverse a list
list3 = [4, -3, 2]
q3 = sorted(list3, 
            reverse=True, 
            key=list3.index)    # Get index of each element to sort
print(q3)