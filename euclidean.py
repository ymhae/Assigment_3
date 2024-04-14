def euclidean_algorithm(a, b):
    """
    Function to calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean Algorithm.

    Parameters:
    a (int): First positive integer
    b (int): Second positive integer

    Returns:
    int: GCD of the two numbers
    """
    # Repeat until the remainder is zero
    while b != 0:
        # Temporary variable to hold the value of b
        temp = b
        # Update b to be the remainder of a divided by b
        b = a % b
        # Update a to be the value previously held by b
        a = temp
    # When b is zero, a is the GCD
    return a


# Example of using the function
print(euclidean_algorithm(48, 18))  # Should print 6
