"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40  # The expected bake time for the lasagna in minutes.40
PREPARATION_TIME = 2 # baking time for a single layer of lasagna


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers:int)-> int:
    """calculates the total time it is going to take to cook the lasagna
    assuming each layer takes 2 minutes to cook

    Args:
        number_of_layers (int): number of layers we want to have in our lasagna

    Returns:
        int: preparation time
    """
    
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers:int, elapsed_bake_time:int)->int:
    """calculates the total time in minutes spend in kitchen cooking
    

    Args:
        number_of_layers (int): number of layers the lasagna has
        elapsed_bake_time (int): time required to bake the lasagna

    Returns:
        int: time spend in the kitchen
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
