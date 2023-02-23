"""
Emma Lee
A01246983
"""

import doctest

def eratosthenes(integer):
    """
    Display a list of prime numbers.

    A function that displays a list of prime numbers between 0 and inputted integer.

    :param integer: an integer
    :precondition: integer must be a positive integer
    :postcondition: displays a list of prime numbers between 0 and the inputted integer
    :return: list of prime numbers between 0 and the inputted integer
    >>> eratosthenes (20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> eratosthenes (30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> eratosthenes (50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> eratosthenes (100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    list_nums = []
    list_non_primes = []
    for number in range(integer+1):
        list_nums.append(number)

    upper_bound = int(integer ** 0.5)
    for value in range(upper_bound + 1):
        if value == 0 or value == 1:
            list_non_primes.append(value)
        else:
            if value not in list_non_primes:
                multiplier = 2
                while value * multiplier <= integer:
                    list_non_primes.append(value * multiplier)
                    multiplier += 1
    sorted_list = sorted(list(set(list_nums) - set(list_non_primes)))
    return sorted_list

def main():
    doctest.testmod(verbose=True)
    print(eratosthenes(30))


if __name__ == "__main__":
    main()