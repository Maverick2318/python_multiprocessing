#!/usr/bin/env python

def square(x):  
    # calculate the square of the value of x
    return x*x

if __name__ == '__main__':

    numbers = [i for i in range(1000000)]
    
    map(square, numbers)
