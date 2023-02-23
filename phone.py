"""
Emma Lee
A01246983
"""

import doctest


def phone(stringnum):
    """
    Display the phone number.

    A function that displays a phone number string as its numerical equivalent.

    :param stringnum: a phone number string
    :precondition: stringnum must be an alphanumeric value
    :postcondition: displays the phone number string as its numerical equivalent
    :return: phone number string as its numerical equivalent
    >>> phone ("ABC-789-2910")
    '222-789-2910'
    >>> phone ("AEJ-PRA-ZWAB")
    '235-772-9922'
    >>> phone ("604-293-APTB")
    '604-293-2782'
    """
    integer_list = []
    for value in stringnum:
        if value.isalpha():
            if value == "A" or value == "B" or value == "C":
                integer_list.append('2')
            elif value == "D" or value == "E" or value == "F":
                integer_list.append('3')
            elif value == "G" or value == "H" or value == "I":
                integer_list.append('4')
            elif value == "J" or value == "K" or value == "L":
                integer_list.append('5')
            elif value == "M" or value == "N" or value == "O":
                integer_list.append('6')
            elif value == "P" or value == "Q" or value == "R" or value == "S":
                integer_list.append('7')
            elif value == "T" or value == "U" or value == "V":
                integer_list.append('8')
            else:
                integer_list.append('9')
        else:
            integer_list.append(value)
    return ''.join(integer_list)


def main():
    doctest.testmod(verbose=True)
    print(phone("604-293-APTB"))


if __name__ == "__main__":
    main()