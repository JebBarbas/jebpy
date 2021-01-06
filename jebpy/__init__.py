"""
jebpy

This module contains more modules that help you doing difficult task

instalation
pip install jebpy

input_types
Different types of input() to capture in the console, capture the
type of data that you want without write convertions nor try/except blocks to prevent the user
to write a different type of data that the one you want.
    Contains:
        - input_str (function)
        - input_str_required (function)
        - input_int (function)
        - input_float (function)
        - input_bool (function)
        - input_yesno (function)

is_string
Check if the given string is an email, password, #HEX color and more without 
write any conditionals or regex expressions. (Uses module re)
    Contains:
        - is_custom (function)
        - is_phone_number (function)
        - is_email (function)
        - is_password (function)
        - is_hex_color_3 (function)
        - is_hex_color_6 (function)
        
password_generator
Generate a random string of the length that you want. (Uses module random)
    Contains:
        - generate_password (function)

percentage
Introduces the PercentageVar, a special type of variable to use percentages and probabilities,
also includes the WeightOption to use in the WeightSelector, to make random choices based in weights, you can
also roll a dice() or flip a coin(). (Uses module random)
    Contains:
        - PerVar (class)
        - WeightOption (class)
        - WeightSelector (class)
        - dice (function)
        - coin (function)
"""

import jebpy
__version__ = 'v1.0.0'
__all__ = ['input_types','is_strings','password_generator','percentage']
