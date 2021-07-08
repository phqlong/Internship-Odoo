# Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. 
# Iterator is an object, which is used to iterate over an iterable object using __next__() method. 
# Iterators have __next__() method, which returns the next item of the object.

# Note that every iterator is also an iterable, but not every iterable is an iterator. 
# For example, a list is iterable but a list is not an iterator. 
# An iterator can be created from an iterable by using the function iter(). 
# To make this possible, the class of an object needs either a method __iter__, 
# which returns an iterator, or a __getitem__ method with sequential indexes starting with 0.


class MyIterator ():
    def __init__(self, iterable):
        self.iterable = iterable
        self.len = len(iterable)

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < self.len:
            value = self.iterable[self.idx]
            self.idx += 1
            return value
        else:
            raise StopIteration

# Create my object
iterable_obj = [1, 'a', True]
my_obj = MyIterator(iterable_obj)

# Create an iterable from my object
my_iterator = iter(my_obj)

# Using next to get to the next iterator element
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Using for loop to get iterator item
for i in my_obj:
    print(i)

# Iterator is exhausted -> raise error
print(next(my_iterator))