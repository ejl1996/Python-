"""
Emma Lee
A01246983
"""

import doctest


def moneychanger(amount):
    """
    Output the fewest bill and coin denominations needed.

    A function that outputs a list of the fewest bill and coin denominations needed to represent a Canadian money amount.

    :param amount: a Canadian money amount
    :precondition: amount must be a positive float with only 2 decimal places
    :postcondition: outputs a list of the fewest bill and coin denominations needed to represent a Canadian money amount
    :return: list of the fewest bill and coin denominations needed to represent a Canadian money amount
    >>> moneychanger (10.51)
    [0, 0, 0, 1, 0, 0, 0, 2, 0, 0]
    >>> moneychanger (66.53)
    [0, 1, 0, 1, 1, 0, 1, 2, 0, 1]
    >>> moneychanger (120.25)
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    """
    # round the amount to the nearest nickle ($0.05) at the beginning
    if amount % 0.05 > 0.02:
        amount = amount + (amount % 0.05)

    listamount = []
    hundred_count = int(amount // 100)
    hundred_remainder = amount % 100
    listamount.append(hundred_count)

    fifty_count = int(hundred_remainder // 50)
    fifty_remainder = hundred_remainder % 50
    listamount.append(fifty_count)

    twenty_count = int(fifty_remainder // 20)
    twenty_remainder = fifty_remainder % 20
    listamount.append(twenty_count)

    ten_count = int(twenty_remainder // 10)
    ten_remainder = twenty_remainder % 10
    listamount.append(ten_count)

    five_count = int(ten_remainder // 5)
    five_remainder = ten_remainder % 5
    listamount.append(five_count)

    two_count = int(five_remainder // 2)
    two_remainder = five_remainder % 2
    listamount.append(two_count)

    one_count = int(two_remainder // 1)
    one_remainder = two_remainder % 1
    listamount.append(one_count)

    twenty_five_count = int(one_remainder // 0.25)
    twenty_five_remainder = one_remainder % 0.25
    listamount.append(twenty_five_count)

    ten_count = int(twenty_five_remainder // 0.10)
    ten_remainder = twenty_five_remainder % 0.10
    listamount.append(ten_count)

    five_count = int(ten_remainder // 0.05)
    listamount.append(five_count)

    return listamount


def main():
    doctest.testmod(verbose=True)
    print(moneychanger(120.23))


if __name__ == "__main__":
    main()