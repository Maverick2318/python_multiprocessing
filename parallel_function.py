#!/usr/bin/env python3

from multiprocessing import Pool

def square(x):  
    # calculate the square of the value of x
    return x*x

if __name__ == '__main__':

    numbers = [i for i in range(1000000)]
    
    with Pool() as pool:
        sqrt_ls = pool.map(square, numbers)
