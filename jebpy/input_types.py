"""
This module provides functions that help with the task of the console input.
- input_str: Try to get a string input that matches with the validation function
- input_str_required: Try to get a string input that matches with the validation function and isn't empty
- input_int: Try to get an integer input that matches with the validation function
- input_float: Try to get a float input that matches with the validation function
- input_bool: Try to get a bolean input that matches with the validation function
- input_yesno: Try to get a string that must be 'y','yes','n' or 'no' and that matches with the validation function
"""
def __input_x(function_to_decorate):
    """
    Decorator to create a new input function.
    """
    def input_x(prompt='',validation_function=lambda x: True,exception_function=lambda x: None,success_function=lambda x: None):
        value = None
        try:
            _input_ = input(prompt).strip()
            value = function_to_decorate(_input_)
            if validation_function(value):
                success_function(value)
                return value
            else:
                raise Exception
        except:
            exception_function(_input_)
            return input_x(prompt, validation_function, exception_function, success_function)
    return input_x

@__input_x
def input_str(x):
    """
    Try to get a string input that matches with the validation function.
    * If not validation given, any string will work
    * If there are any error, executes the optional exception_function with the input as parameter
    * If success, executes the optional success_function with the input as parameter

    Args: 
        (optional) prompt (Any): The prompt that you'd use in a normal input() function
        (optional) validation_function (function): A function used to check if the input meets the conditions, for default always return True
        (optional) exception_function (function): A function used when there is any error converting the input or when the validation_function returns False
        (optional) success_function (function): A function used when the input is successfuly converted and returned
    Returns:
        A string value
    Examples:
        >>> input_str('Write your name: ', lambda x: len(x) > 0, lambda x: print('An input is required'))
        Write your name: 
        An input is required
        Write your name: John Doe
        >>>
    """
    return str(x)

@__input_x
def input_str_required(x):
    """
    Try to get a string input that matches with the validation function and that is not an empty string.
    * If not validation given, any string that isn't empty will work
    * If there are any error, executes the optional exception_function with the input as parameter
    * If success, executes the optional success_function with the input as parameter

    Args: 
        (optional) prompt (Any): The prompt that you'd use in a normal input() function
        (optional) validation_function (function): A function used to check if the input meets the conditions, for default always return True
        (optional) exception_function (function): A function used when there is any error converting the input or when the validation_function returns False
        (optional) success_function (function): A function used when the input is successfuly converted and returned
    Returns:
        A string value
    Examples:
        >>> input_str_required('Write your last name: ', lambda x: print('An input is required'))
        Write your last name: 
        An input is required
        Write your name: Doe
        >>>
    """
    if len(x) > 0:
        return str(x)
    else:
        raise ValueError

@__input_x
def input_int(x):
    """
    Try to get an integer input that matches with the validation function.
    * If not validation given, any integer will work
    * If there are any error, executes the optional exception_function with the input as parameter
    * If success, executes the optional success_function with the input as parameter

    Args: 
        (optional) prompt (Any): The prompt that you'd use in a normal input() function
        (optional) validation_function (function): A function used to check if the input meets the conditions, for default always return True
        (optional) exception_function (function): A function used when there is any error converting the input or when the validation_function returns False
        (optional) success_function (function): A function used when the input is successfuly converted and returned
    Returns:
        An integer value
    Examples:
        >>> input_int('Write how many years do you have: ', lambda x: x >= 0, lambda x: print(x + ' is not a valid age'))
        Write how many years do you have: lorem ipsum
        lorem ipsum is not a valid age
        Write how many years do you have: -1
        -1 is not a valid age
        Write how many years do you have: 10
        >>>
    """
    return int(x)

@__input_x
def input_float(x):
    """
    Try to get a float input that matches with the validation function.
    * If not validation given, any float will work
    * If there are any error, executes the optional exception_function with the input as parameter
    * If success, executes the optional success_function with the input as parameter

    Args: 
        (optional) prompt (Any): The prompt that you'd use in a normal input() function
        (optional) validation_function (function): A function used to check if the input meets the conditions, for default always return True
        (optional) exception_function (function): A function used when there is any error converting the input or when the validation_function returns False
        (optional) success_function (function): A function used when the input is successfuly converted and returned
    Returns:
        A float value
    Examples:
        >>> input_float('How much costs an apple? ', lambda x: x > 0, lambda x: print('The price must be valid and greater than 0'))
        How much costs an apple? lorem ipsum
        The price must be valid and greater than 0
        How much costs an apple? 0
        The price must be valid and greater than 0
        How much costs an apple? 1.99
        >>>
    """
    return float(x)

@__input_x
def input_bool(x):
    """
    Try to get a boolean input that matches with the validation function.
    * If not validation given, any boolean will work
    * If there are any error, executes the optional exception_function with the input as parameter
    * If success, executes the optional success_function with the input as parameter

    Args: 
        (optional) prompt (Any): The prompt that you'd use in a normal input() function
        (optional) validation_function (function): A function used to check if the input meets the conditions, for default always return True
        (optional) exception_function (function): A function used when there is any error converting the input or when the validation_function returns False
        (optional) success_function (function): A function used when the input is successfuly converted and returned
    Returns:
        A boolean value
    Examples:
        >>> input_bool('Do you have sisters? ', exception_function=lambda x: print('Write True or False'))
        Do you have sisters? yes
        Write True or False
        Do you have sisters? True
        >>>
    """
    boolean_text = x
    if boolean_text == 'True':
        return True
    elif boolean_text == 'False':
        return False
    else:
        raise ValueError

@__input_x
def input_yesno(x):
    """
    Try to get a string input that must be 'y','yes','n' or 'no' and matches with the validation function.
    * If not validation given, any boolean will work
    * If there are any error, executes the optional exception_function with the input as parameter
    * If success, executes the optional success_function with the input as parameter
    * 'y' and 'yes' return True
    * 'n' and 'no' return False
    * The answers are case-insensitive, so, the function takes 'yes', 'Yes', 'yEs' and 'YES' as the same

    Args: 
        (optional) prompt (Any): The prompt that you'd use in a normal input() function
        (optional) validation_function (function): A function used to check if the input meets the conditions, for default always return True
        (optional) exception_function (function): A function used when there is any error converting the input or when the validation_function returns False
        (optional) success_function (function): A function used when the input is successfuly converted and returned
    Returns:
        A boolean value
    Examples:
        >>> input_yesno('Do you have sisters? (yes/no) ', exception_function=lambda x: print('Type yes or no'))
        Do you have sisters? lorem ipsum
        Type y or n
        Do you have sisters? YES
        >>>
    """
    text = x
    if text.lower() == 'y' or text.lower() == 'yes':
        return True
    elif text.lower() == 'n' or text.lower() == 'no':
        return False
    else:
        raise ValueError

if __name__ == '__main__':
    print('TESTING FUNCTIONS ...')

    print('\tTESTING STRING FUNCTION ...')
    input_str('Case 1: Write a string: ')
    input_str('Case 2: Write a string (required): ', lambda x: len(x) > 0)

    print('\tTESTING INT FUNCTION ...')
    input_int('Case 1: Write an integer: ')
    input_int('Case 2: Write an integer greater than 0 and less than 10: ', lambda x: x > 0 and x < 10)

    print('\tTESTING FLOAT FUNCTION ...')
    input_float('Case 1: Write a float: ')
    input_float('Case 2: Write a negative float: ', lambda x: x < 0)

    print('\tTESTING BOOLEAN FUNCTION ...')
    input_bool('Case 1: Write a boolean: ')
    input_bool('Case 2: Write a boolean (It has to be False): ', lambda x: not x)

    print('\tTESTING YESNO FUNCTION ...')
    input_yesno('Case 1: Write y/yes/n/no: ')
    input_yesno('Case 2: Write y/yes: ', lambda x: x)
