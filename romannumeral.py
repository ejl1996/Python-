"""
Emma Lee
A01246983
"""

import doctest

denominations = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


def romannumeral(positive_integer):
    """
    Output the Roman numeral equivalent of an integer.

    A function that outputs the Roman numeral equivalent of an integer.

    :param positive_integer: an integer
    :precondition: positive_integer must be a positive integer in the range [1, 10000]
    :postcondition: converts the integer to its Roman numeral equivalent
    :return: Roman numeral equivalent of an integer
    >>> romannumeral(2)
    'II'
    >>> romannumeral(100)
    'C'
    >>> romannumeral(999)
    'CMXCIX'
    """
    result = []

    if positive_integer >= 1000:
        count = positive_integer // 1000
        result.append('M' * count)
        positive_integer %= 1000
    if positive_integer >= 900:
        count = positive_integer // 900
        result.append('CM' * count)
        positive_integer %= 900
    if positive_integer >= 500:
        count = positive_integer // 500
        result.append('D' * count)
        positive_integer %= 500
    if positive_integer >= 400:
        count = positive_integer // 400
        result.append('CD' * count)
        positive_integer %= 400
    if positive_integer >= 100:
        count = positive_integer // 100
        result.append('C' * count)
        positive_integer %= 100
    if positive_integer >= 90:
        count = positive_integer // 90
        result.append('XC' * count)
        positive_integer %= 90
    if positive_integer >= 50:
        count = positive_integer // 50
        result.append('L' * count)
        positive_integer %= 50
    if positive_integer >= 40:
        count = positive_integer // 40
        result.append('XL' * count)
        positive_integer %= 40
    if positive_integer >= 10:
        count = positive_integer // 10
        result.append('X' * count)
        positive_integer %= 10
    if positive_integer >= 9:
        count = positive_integer // 9
        result.append('IX' * count)
        positive_integer %= 9
    if positive_integer >= 5:
        count = positive_integer // 5
        result.append('V' * count)
        positive_integer %= 5
    if positive_integer >= 4:
        count = positive_integer // 4
        result.append('IV' * count)
        positive_integer %= 4
    if positive_integer >= 1:
        count = positive_integer // 1
        result.append('I' * count)
        positive_integer %= 1
    final_result = ''.join(result)
    return final_result


def main():
    doctest.testmod(verbose=True)
    print(romannumeral(1))
    print(romannumeral(2))
    print(romannumeral(3))
    print(romannumeral(4))
    print(romannumeral(5))
    print(romannumeral(6))
    print(romannumeral(7))
    print(romannumeral(8))
    print(romannumeral(9))
    print(romannumeral(10))
    print(romannumeral(11))
    print(romannumeral(20))
    print(romannumeral(30))
    print(romannumeral(40))
    print(romannumeral(50))
    print(romannumeral(60))
    print(romannumeral(70))
    print(romannumeral(80))
    print(romannumeral(90))
    print(romannumeral(100))
    print(romannumeral(200))
    print(romannumeral(300))
    print(romannumeral(400))
    print(romannumeral(500))
    print(romannumeral(600))
    print(romannumeral(700))
    print(romannumeral(800))
    print(romannumeral(900))
    print(romannumeral(999))
    print(romannumeral(1000))

if __name__ == '__main__':
    main()
