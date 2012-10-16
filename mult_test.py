"""
Test how much time multiplication takes progressively
"""

from time import time
from random import random
from numpy import array, dot

class Computer(object):
    def __init__(self):
        pass

    def compute(self, vector1, vector2, dim, times, with_numpy):
        if with_numpy:
            v1 = array(vector1.vector)
            v2 = array(vector2.vector)
            
        start_time = time()
        for i in xrange(0, times):
            if with_numpy:
                accumulator = dot(v1, v2)
            else:
                accumulator = 1
                for j in range(1, len(vector1.vector)):
                    accumulator += vector1.vector[j] * vector2.vector[j]

        end_time = time()
        elapsed_time = end_time - start_time
        self.display(dim, times, elapsed_time)

    def display(self, dim, times, elapsed_time):
        print 'Multiplying 2 {0}-d vectors {1} times took {2} seconds'.format(dim, times, elapsed_time)

class Vector(object):
    def __init__(self, dim):
        self.vector = []
        for i in xrange(0, dim):
            self.vector.append(random())

        print '{0}-d vector constructed'.format(len(self.vector))

def compute_repeated(computer, vector1, vector2, with_numpy):
    if with_numpy:
        print '\nnumpy.dot\n'
    else:
        print '\npure Python\n'
    for i in xrange(0, 300001, 50000):
        computer.compute(vector1, vector2, len(vector1.vector), i, with_numpy)

def main():
    vector1 = Vector(100)
    vector2 = Vector(100)

    computer = Computer()
    compute_repeated(computer, vector1, vector2, True)
    compute_repeated(computer, vector1, vector2, False)

if __name__ == '__main__':
    main()
                
