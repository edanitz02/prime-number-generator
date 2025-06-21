#filename: mersenne_v0_6_20_2025
#ancestor: primes_v0_6_17_25
# Author: Ethan Danitz
# 
# """ This prime number generator uses known prime numbers to check for more prime 
# numbers. It calculates the prime numbers less than 10,000,000 and times how long
# it takes to compare the efficiency of versions. """


# import math
# import time

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

# def check_prime(n, primes):
#     prime = False                          # track return value
#     sqrt = math.floor(math.sqrt(n))        # greatest possible factor (GPF)
#     for i in primes:                       # loop through list of primes
#         if(n % i == 0):                    # check if n is divisible by prime
#             break                          # not prime, return False
#         if(sqrt < i):                      # Check if current prime is above GPF
#             prime = True                   # Set prime to true and return
#             break
#     return prime 

# def call_primes():
#     primes = [2, 3, 5]                     # Define list of primes
#     for i in range(7, 10000000, 2):        # Iteration through odd numbers
#         if (i % 5 == 0):                   # Skip odd numbers ending in 5
#             continue
#         if (check_prime(i, primes)):       # if odd number is prime
#             primes.append(i)               #  add it to primes
#     return primes                          # return list of primes


# # main: 
# start = time.time()                        # get before time
# primes = call_primes()                     # calculate primes
# end = time.time()                          # get after time

# total = end - start                        # total time it ran for
# print(f"There are 664579 primes under 10,000,000, we found {len(primes)}")
# if (len(primes) == 664579):                # check if it found correct # of primes
#     print("Success!")
# else:
#     print("Incorrect code")
# print(f"The primes from 7 - 10,000,000 found in {total} seconds.")


# """ This code calculates the Mersenne Primes under 70, with a loop through every odd 
# number n 3-70 where n and 2**n-1 are both checked for prime. The check_prime
# method returns false for all even numbers and checks the candidate for divisibility 
# with every odd number within 3 and the square root of the candidate. """

import math

mersenne = []

def check_prime(n):
    prime = False                          # track return value
    if (n % 2 != 0):                       # filters out even numbers
        prime = True                       # set prime to True before loop
        sqrt = math.floor(math.sqrt(n))    # greatest necessary factor (GNF)
        for i in range(3, sqrt, 2):        # loop through list of odds
            if(n % i == 0):                # check n's divisibility
                prime = False              # set prime to False and return
                break
    return prime

def call_prime():
    for i in range(3, 70, 2):
        if(check_prime(i) and check_prime(2**i-1)):
            mersenne.append(i)

call_prime()
print(mersenne)