# Prime Number Generator
# Author: Ethan Danitz
# Last Modified: 6/19/25
# v1.0.0
# 
# """ This prime number generator uses known prime numbers to check for more prime 
# numbers. It calculates the prime numbers less than 10,000,000 and times how long
# it takes to compare the efficiency of versions. """


import math
import time

# def check_prime(n, primes):  old code with many return statements
#     # get the greatest possible factor
#     sqrt = math.floor(math.sqrt(n))
#     # loop through a list of prime numbers
#     for i in primes:
#         # if it's divisible by a prime, not prime
#         if(n % i == 0):
#             return False
#         # Check if current prime is greater then the candidate sqrt
#         if(sqrt < i):
#             return True
#     # failsafe: return not prime
#     return False

def check_prime(n, primes):
    prime = False                          # track return value
    sqrt = math.floor(math.sqrt(n))        # greatest possible factor (GPF)
    for i in primes:                       # loop through list of primes
        if(n % i == 0):                    # check if n is divisible by prime
            break                          # not prime, return False
        if(sqrt < i):                      # Check if current prime is above GPF
            prime = True                   # Set prime to true and return
            break
    return prime 

def call_primes():
    primes = [2, 3, 5]                     # Define list of primes
    for i in range(7, 10000000, 2):        # Iteration through odd numbers
        if (i % 5 == 0):                   # Skip odd numbers ending in 5
            continue
        if (check_prime(i, primes)):       # if odd number is prime
            primes.append(i)               #  add it to primes
    return primes                          # return list of primes


# main: 
start = time.time()                        # get before time
primes = call_primes()                     # calculate primes
end = time.time()                          # get after time

total = end - start                        # total time it ran for
print(f"There are 664579 primes under 10,000,000, we found {len(primes)}")
if (len(primes) == 664579):                # check if it found correct # of primes
    print("Success!")
else:
    print("Incorrect code")
print(f"The primes from 7 - 10,000,000 found in {total} seconds.")

