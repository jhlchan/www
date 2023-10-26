#!/usr/bin/env python3

# Print series of prime numbers in python
# https://stackoverflow.com/questions/11619942/

import math

def primes_to(n):
    primes = []
    primes.append(2) # the only even prime
    for num in range(3,n + 1,2): # all odd primes <= n, from 3, step 2
        if all (num%j != 0 for j in range(3,int(math.sqrt(num))+1,2)):
            primes.append(num) # pick up the odd prime

    return primes

print('Primes up to 100:')
print(primes_to(100))