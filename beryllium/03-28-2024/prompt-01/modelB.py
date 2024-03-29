def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    prime_numbers = [True] * (n + 1)
    prime_numbers[0] = prime_numbers[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime_numbers[i]:
            for j in range(i**2, n + 1, i):
                prime_numbers[j] = False

    prime_numbers = [i for i in range(2, n + 1) if prime_numbers[i]]
    return prime_numbers


input_list = [2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = sieve_of_eratosthenes(max(input_list))
result = [number for number in input_list if number in prime_numbers]
print(result)
