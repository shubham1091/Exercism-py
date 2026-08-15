def steps(number):
    """this function takes any positive number and returns number of step it will take to become 1 following the rules of collatz conjecture
    
    rules: 
        if the number is even divide it by 2
        if it's odd then multiply it by 3 and add 1

    Args:
        number (int): any positive number
        
    return:
        step to reach 1
    """
    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    
    if number == 1:
        return 0
    elif number % 2 == 0:
        return steps(number//2) + 1
    else:
        return steps(number*3 + 1) + 1
