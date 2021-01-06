"""
This module contains functions to check if a string is some type of entry
- is_custom: Checks if the given text matches with a given regex
- is_phone_number: Checks if the given text is a phone number
- is_email: Checks if the given text is an email
- is_password: Checks if the given text is a good password
- is_hex_color_3: Checks if the given text is an hexadecimal color of 3 values (#RGB)
- is_hex_color_6: Checks if the given text is an hexadecimal color of 6 values (#RRGGBB)
"""
import re

def is_custom(text, regex):
    """
    Checks if the given text matches with a given regex

    Args:
        text (str): The text to match
        regex (str): A regular expression that you wanna match (recomended a raw string: r'')
    Returns:
        A boolean value, True if the text matches the string or False if not
    Raises:
        TypeError: If not text or regex given
    """
    return True if re.match(regex, text.strip()) else False

def is_phone_number(text,format=1):
    """
    Checks if the given text is a phone number
    * The phone must be for default in format (000)0000000, but it can be changed

    Args:
        text (str): The text to match
        (optional) format (int): The number of the phone format that you want to check, default 1 (see below the formats)
    Returns:
        A boolean value, True if the text is a phone number in the specified format or False if not
    Raises:
        TypeError: If not text given
        KeyError: If the given format doesn't exists or is different that an integer
    Formats (# can be any 0-9 number):
        0: ##########
        1: (###)#######
        2: (###)-###-####
        3: (###) ### ####
        4: ###-###-####
        5: ### ### ####
        6: (###)###-####
        7: (###)### ####
    """
    formats = {
        0: r'^\d{10}$',
        1: r'^\(\d{3}\)\d{7}$',
        2: r'^\(\d{3}\)-\d{3}-\d{4}$',
        3: r'^\(\d{3}\) \d{3} \d{4}$',
        4: r'^\d{3}-\d{3}-\d{4}$',
        5: r'^\d{3} \d{3} \d{4}$',
        6: r'^\(\d{3}\)\d{3}-\d{4}$',
        7: r'^\(\d{3}\)\d{3} \d{4}$',
    }
    return True if re.match(formats[format],text.strip()) else False

def is_email(text):
    """
    Checks if the given text is an email
    * The email is checked in the format: example@example.exa

    Args:
        text (str): The text to match
    Returns:
        A boolean value, True if the text matches and False if not
    Raises:
        TypeError: If not text given
    """
    regex = r'^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'
    return True if re.match(regex,text.strip()) else False

def is_password(text):
    """
    Checks if the given text is a good password:
    * Minimum 8 characters
    * At least one uppercase letter
    * At least one lowercase letter
    * At least one number

    Args:
        text (str): The text to match
    Returns:
        A boolean value, True if the text matches and False if not
    Raises:
        TypeError: If not text given
    """
    regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$'
    return True if re.match(regex,text.strip()) else False

def is_hex_color_3(text):
    """
    Checks if the given text is an hexadecimal color of 3 values (#RGB)

    Args:
        text (str): The text to match
    Returns:
        A boolean value, True if the text matches and False if not
    Raises:
        TypeError: If not text given
    """
    regex = r'^#[a-fA-F0-9]{3}$'
    return True if re.match(regex,text.strip()) else False

def is_hex_color_6(text):
    """
    Checks if the given text is an hexadecimal color of 6 values (#RRGGBB)

    Args:
        text (str): The text to match
    Returns:
        A boolean value, True if the text matches and False if not
    Raises:
        TypeError: If not text given
    """
    regex = r'^#[a-fA-F0-9]{6}$'
    return True if re.match(regex,text.strip()) else False

if __name__ == '__main__':
    def resultado(function='',text=''):
        if function(text):
            print('Si es')
        else:
            print('No es')
    print('TESTING FUNCTIONS ...')

    print('\tTESTING PHONE FUNCTION ...')
    resultado(is_phone_number,input('Write a phone number: '))

    print('\tTESTING EMAIL FUNCTION ...')
    resultado(is_email, input('Write an email: '))

    print('\tTESTING PASSWORD FUNCTION ...')
    resultado(is_password, input('Write a password: '))

    print('\tTESTING COLOR FUNCTIONS ...')
    resultado(is_hex_color_3,input('Write a color in format #RGB'))
    