"""
This module provides password generators
- generate_password: Generate a password
"""
from random import randint

__characters = (
    '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',
    'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
    'W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_'
)
__MAX_BASE = len(__characters)

def generate_password(length,base=__MAX_BASE):
    """
    Generate a password.
    * If the given base is less than 1, 1 will be the value
    * If the given base is greater than the length of MAX_BASE, MAX_BASE will be the value
    * The actual value of MAX_BASE is: 64

    Args:
        length (int): The length of the password
        (optional) base (int): The number of different characters that the password will have, default is MAX_BASE
    Returns:
        A string of {length} characters
    Raises:
        TypeError: When not giving the {length} argument
        ValueError: When the given {length} argument is not an integer value
    Examples:
        >>> print(generate_password(10))
        7q4UCwW0PK
        >>> print(generate_password(10,2))
        0100100101
        >>> print(generate_password(6,16))
        87A39E
    """
    password = ''

    if base < 1:
        base = 1
    elif base > __MAX_BASE:
        base = __MAX_BASE

    for i in range(length):
        password += __characters[randint(0,base-1)]
    return password

if __name__ == "__main__":
    print('TESTING FUNCTIONS ...')

    print('TESTING PASSWORD FUNCTION ...')
    
    for i in range(1,17):
        print(generate_password(i))

    generate_password(12.3)
   