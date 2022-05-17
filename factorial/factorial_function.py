def factorial(num: int) -> int:
    """
    Calculates the factorial of a num.
    :param num: must be int and greater than 0
    :return: factorial of the number
    """

    if not isinstance(num, int):
        raise ValueError("factorial() only accepts integral values")
    if num < 0:
        raise ValueError("factorial() not defined for negative values")

    curr = 1
    for i in range(1, num + 1):
        curr *= i

    return curr
