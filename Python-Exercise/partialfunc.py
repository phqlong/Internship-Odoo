# Use partial function from functools module to rewrite the method for doubleNum and tripleNum
from functools import partial

def multiply(x, y):
    return x * y

def doubleNum(x):
    return multiply(x, 2)

def tripleNum(x):
    return multiply(x, 3)

newDoubleNum = partial(multiply, y=2)
print(newDoubleNum(69))

newTripleNum = partial(multiply, 3)
print(newTripleNum(69))