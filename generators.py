# File: generators.py
# Description: Examples on how to create and use generators in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Examples on how to create and use generators in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Generators_in_Python (date of access: XX.XX.XXXX)


from random import random


# Creating the class for iterations
class RandomIterator:
    # We add the method __iter__ if we want to iterate this class
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


# Creating function as generator
# Instead of return we use yield
# In this way we remember the order till yield each time we call the function
def random_generator(k):
    for i in range(k):
        yield random()


# Creating instance of class
gen = random_generator(3)
print(type(gen))

for i in gen:
    print(i)


# More clear example about remembering the yield the order
def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    #return 'No more elements'
    yield 2
    print('Checkpoint 3')


g = simple_gen()
x = next(g)
print(x)
y = next(g)
print(y)
z = next(g)


# Implementing the task - creating the methods for prime numbers
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2, 2):
        if n % i == 0:
            return False
    return True


def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

