#!/usr/bin/env python3

# Print series of prime numbers in python
# https://stackoverflow.com/questions/11619942/

import math

print (2, end=' ')  # the only even prime

# all the odd primes less than 101, from 3, step 2
for num in range(3,101,2):
    if all (num%j != 0 for j in range(3,int(math.sqrt(num))+1, 2)):
        print (num, end=' ')

# last newline
print ()