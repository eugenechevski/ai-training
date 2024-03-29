def sieve_of_eratosthenes(n):
    # Create a list of consecutive integers from 2 to n
    sieve = [True] * (n + 1)

    # Set 0 and 1 as non-prime
    sieve[0] = sieve[1] = False

    # Loop through each number from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If the number is prime, mark all its multiples as non-prime
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Create a new list to store all the prime numbers
    primes = []

    # Loop through the sieve and append all the prime numbers to the list
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)

    return primes

# Example usage:
print(sieve_of_eratosthenes(100))