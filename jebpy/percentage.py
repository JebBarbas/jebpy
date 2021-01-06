"""
This module provides help with percentages
- PerVar: A class to create your probability type variable
- WeightOption: A class to create an option to the WeightSelector
- WeightSelector: A class to create a random selector of options with weight
- dice: Roll a dice and returns a number from 1 to {sides}
- coin: Returns True or False with a 50% of probability of each one
"""
from random import randint, choices

class PerVar:
    """
    A percentage type variable.
    """

    # Constructor
    def __init__(self, value):
        """
        Constructor of PerVar class
        * Uses self.set() to set the value, if you have problems with the constructor see self.set()
        """
        self.set(value)

    # Setter and getter
    def set(self, value):
        """
        Set the value of the percentage

        Args:
            value (float|int): The value of the percentage
        Raises:
            TypeError: When not giving the {value} argument or this argument is not an integer o float value
            ValueEror: When the given argument {value} is neither integer nor float
        """    
        self.__value = float(value)
    def get(self):
        """
        Get the value of the percentage

        Returns:
            A float number
        """
        return self.__value

    # Normal methods
    def probability(self):
        """
        Return a boolean value
        * There are a {self.get()}% probability to return True

        Returns:
            A boolean value
        """
        return self.get() > float(randint(0,99))

    def roll(self):
        """
        Alias for PerVar().probability()
        """
        self.probability()

    def rot(self):
        """
        Alias for {self.get()*0.01}
        * The name rot is from "Rule of Three"
        * The rot is calculated based on:
            if 100 is 1, then {self.get()} is {self.rot()}

        Returns:
            A float value
        Examples of Use:
            discount = PerVar(50)
            final_price = price * discount.rot()
        """
        return self.get() * 0.01

    # Static methods
    @staticmethod
    def merge(*percentages):
        """
        Merge 2 or more percentages
        * The way this merge the percentages is very easy: if one percentage is 50% and another one is 75%, this will return a new percentage with a value of the 50% of 75% (37.5%) 
        * If only 1 PerVar given, returns the same

        Args:
            percentages (PerVar(s)): Two or more PerVar
        Returns:
            A new PerVar instance
        Raises:
            TypeError: When you don't give any argument or when some of the arguments isn't a PerVar
        Examples:
            >>> per_1 = PerVar(10)
            >>> per_2 = PerVar(25)
            >>> per_3 = PerVar(50)

            >>> per_4 = PerVar.merge(per_1, per_3)
            >>> per_5 = PerVar.merge(per_1, per_2, per_3)

            print(per_4)
            5.0

            print(per_5)
            1.25
        """
        if len(percentages) <= 0:
            raise TypeError('you need to give at least 1 PerVar')

        for percentage in percentages:
            if not isinstance(percentage, PerVar):
                raise TypeError('all the arguments need to be of type PerVar')

        if len(percentages) == 1:
            return percentages[0]
        else:
            new_percentage = 1.0
            for percentage in percentages:
                new_percentage *= percentage.rot()

            return PerVar(PerVar.value_from_rot(new_percentage))
    @staticmethod
    def value_from_rot(rot):
        """
        Return a base 100 value for a PerVar based on a base 1 rot

        Args:
            rot (float): A number (1 will be converted in 100)
        Returns:
            A float value
        Raises:
            TypeError: If the given rot is not a number or is not given
        """
        return rot/0.01

    # Magic methods
    def __str__(self):
        return str(self.get())

class WeightOption:
    """
    An option to the WeightSelector
    """
    def __init__(self,item,weight):
        """
        Initialice the option

        Args:
            item (Any): The item that the WeightSelector will return
            weight (int): The weight of the option
        """
        self.item = item
        self.weight = int(weight)

        self.tup = (self.item, self.weight)

    def __str__(self):
        return f'Item: {self.item} with a weight of: {self.weight} '

class WeightSelector:
    """
    A selector of WeightOption(s)
    """
    def __init__(self, *options):
        """
        Initialice the selector

        Args:
            options (WeightOption(s)): All the instances of WeightOptions that you want
        """
        self.options = options

    def choose(self):
        """
        Pick an option from all of the WeightSelector (the weight of each WeightOption matters)

        Returns:
            The WeightOption.item
        Raises:
            TypeError: If one of the options in the WeightSelector is not a WeightOption instance
        """

        if self.__all_options():
            items = []
            weights = []
            for option in self.options:
                items.append(option.item)
                weights.append(option.weight)
            
            items = tuple(items)
            weights = tuple(weights)

            return choices(population = items,weights=weights)[0]

    def choose_no_weight(self):
        """
        The same as {self.choose()} but the weights don't matter, so it can choose any WeightOption with same probability
        Returns:
            The WeightOption.item
        Raises:
            TypeError: If one of the options in the WeightSelector is not a WeightOption instance
        """
        if self.__all_options():
            items = []
            for option in self.options:
                items.append(option.item)
            
            items = tuple(items)

            return choices(population = items)[0]

    def __all_options(self):
        """
        Checks if all the options in the WeightSelector are WeightOption instances

        Returns:
            True (if all the options are instances, if one of them isn't raise an error)
        Raises:
            TypeError: One option in the WeightSelector is not a WeightOption instance
        """
        for option in self.options:
            if not isinstance(option, WeightOption):
                raise TypeError('all options must be a WeightOption instance')
        return True


def dice(sides=6):
    """
    Roll a dice and returns a number from 1 to {sides}

    Args:
        (opcional) sides (int): The number of sides that the dice is gonna have, default is 6
    Returns:
        An integer between 1 and {sides}, include both sides
    Raises:
        TypeError: If the given argument for {sides} is not an integer number
    """
    return randint(1,int(sides))

def coin():
    """
    Returns True or False with a 50% of probability of each one
    * There is a 50% of probability that returns True and another 50% to return False

    Returns:
        A boolean value
    """
    _coin = PerVar(50)
    return _coin.probability()

if __name__ == "__main__":
    print('TESTING FUNCTIONS ...')

    print('\tTESTING PERVAR')
    ten_chance = PerVar(10)
    print(ten_chance.probability())

    print('\tTESTING WEIGHT OPTION AND SELECTOR')
    opc1 = WeightOption(1,100)
    opc2 = WeightOption(2,50)
    opc3 = WeightOption(3,10)
    sel = WeightSelector(opc1,opc2,opc3)
    print(sel.choose())

    print('\tTESTING DICE AND COIN')
    print(dice())
    print(dice(100))

    print(coin())
    