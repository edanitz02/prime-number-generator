# uses known prime numbers to check for more prime numbers
import math
import time

def check_prime(n, primes):
    # get the greatest possible factor
    sqrt = math.floor(math.sqrt(n))
    # loop through a list of prime numbers 
    for i in primes:
        # if it's divisible by a prime, not prime
        if(n % i == 0):
            return False
        # Check if current prime is greater then the greatest possible factor (is prime!)
        if(sqrt < i):
            return True
    # failsafe: return not prime
    return False

def call_primes():
    # define list of first 3 primes
    primes = [2, 3, 5]
    # iterate through all odd numbers before 10,000,000
    for i in range(7, 10000000, 2):
        # if divisible by 5, skip
        if (i % 5 == 0):
            continue
        # check if number is prime
        if (check_prime(i, primes)):
            # add it to prime number list
            primes.append(i)
    return primes


# main: 
start = time.time()
primes = call_primes()
end = time.time()

total = end - start
print(f"There are 664579 primes under 10,000,000, we found {len(primes)}")
if (len(primes) == 664579):
    print("Success!")
else:
    print("Incorrect code")
print(f"The primes from 7 - 10,000,000 found in {total} seconds.")

