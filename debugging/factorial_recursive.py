#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    This function computes the factorial of a given number `n` using recursion.
    The factorial of a number `n` (denoted as n!) is the product of all positive integers
    less than or equal to `n`. By definition, 0! = 1.

    Parameters:
    -----------
    n (int): The number for which the factorial is to be computed.

    Returns:
    --------
    int: The factorial of the number `n`. If `n` is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the command line argument and convert it to an integer
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)
