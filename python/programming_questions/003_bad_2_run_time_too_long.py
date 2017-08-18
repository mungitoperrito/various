'''
Problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

This version spends an enormous amount of time removing items from the list of
   potential primes. It works for small numbers but crashes before finishing on
   the problem given. See 003_largest_prime_factor.py for a better solution.

Solution:
Dave Cuthbert copyright 2017
License MIT
'''

import math

def create_list_of_primes(maximum_value):
    list_of_values = [i for i in range(2, maximum_value)]

    index = 0
    while index < len(list_of_values):
       current_value =  list_of_values[index]  
       multiplier = 2 
       while (multiplier < ((maximum_value // current_value) + 1)):  
            if (current_value * multiplier) in list_of_values:
                list_of_values.remove(current_value * multiplier)
            else:
                multiplier += 1
       index += 1
        
    return list_of_values


def check_if_prime(number_to_factor):
    primes  = create_list_of_primes(number_to_factor)
    for p in reversed(primes): 
        if (number_to_factor % p == 0):
            return p 
    return -1

    
def solve_problem(number_to_factor):
    largest_prime = check_if_prime(number_to_factor)

    return(largest_prime)


if __name__ == "__main__":
    #NUMBER_TO_FACTOR = 600851475143
    #NUMBER_TO_FACTOR = 214    # 107 largest prime factor
    NUMBER_TO_FACTOR = 20000

    print(solve_problem(NUMBER_TO_FACTOR))
