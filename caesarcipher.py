"""
Emma Lee
A01246983
"""

import string
import doctest

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)

def caesarcipher(message, encode, shift):
    """
    Shift each alphanumeric character in a message.

    A function that shifts each alphanumeric character in a message and displays the hidden message.

    :param message: a string
    :param encode: a Boolean
    :param shift: an integer
    :precondition: message must be a string composed of any combination of characters or be an empty string
    :precondition: encode must be a Boolean that is True or False
    :precondition: shift must be a positive or negative integer
    :postcondition: shifts each alphanumeric character in the message a specified number of places
    :return: if Boolean encode is set to True, returns the encoded cipher; if Boolean encode is set to False, returns the decoded messsage
    >>> caesarcipher('yzaY-ZA890', True, 3)
    'bcdB-CD123'
    >>> caesarcipher('', False, 3)
    ''
    >>> caesarcipher('JEab-BA77', True, 5)
    'OJfg-GF22'
    """
    if not encode:
        shift *= -1  # decode is simply shifting in opposite direction

    output_msg = []
    for char in message:
        if char in numbers:
            char_index = ord(char) - ord('0')
            offset = char_index + shift
            shifted_char = numbers[offset % 10]
        elif char in lowercase_letters:
            char_index = ord(char) - ord('a')
            offset = char_index + shift
            shifted_char = lowercase_letters[offset % 26]
        elif char in uppercase_letters:
            char_index = ord(char) - ord('A')
            offset = char_index + shift
            shifted_char = uppercase_letters[offset % 26]
        else:
            shifted_char = char
        output_msg.append(shifted_char)

    final_message = ''.join(output_msg) #assign variable for output message
    return final_message


def main():
    doctest.testmod(verbose=True)
    print(caesarcipher('PeJA-2390', True, 4))


if __name__ == '__main__':
    main()
