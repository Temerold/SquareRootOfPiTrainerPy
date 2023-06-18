from math import sqrt, pi
from os import system

import decimal


# Thanks to Green Cloak Guy for the algorithm
# (https://stackoverflow.com/a/59845330/11918034)
def square_root(num: float | int, precision: int) -> float:
    # sourcery skip: avoid-single-character-names-variables

    # We need to set the decimal precision to more than enough digits to handle
    # the full calculation (the number of decimal places, plus the number of
    # digits in the original number, should be enough -- this counts the numbers
    # both before and after the decimal point) we add 2 to give some room to
    # spare, as well.
    decimal.getcontext().prec = precision + len(str(num)) + 2

    x = decimal.Decimal(num)
    y = decimal.Decimal(1)
    e = decimal.Decimal(10) ** decimal.Decimal(-precision)
    while x - y >= e:
        x = (x + y) / 2
        y = decimal.Decimal(num) / x
    # Now, truncate to exactly the desired number of digits. We can do this by
    # using the built-in `round` method with `precision`. We subtract `e` / 2 to
    # simulate always rounding down, since `round` simply rounds to the closest.
    return round(x - (e / 2), precision)


def get_appropriate_sqrt(test):
    return str(square_root(pi, len(test) - 2) if len(test) > 2 else sqrt)


if __name__ == "__main__":
    # sourcery skip: avoid-global-variables

    sqrt = square_root(pi, 12)

    while True:
        test = input("> ")
        appropriate_sqrt = get_appropriate_sqrt(test)

        if test == str(sqrt) or (
            len(test) > len(str(sqrt)) and str(square_root(pi, len(test) - 2))
        ):
            input("Correct!")
            break
        print("Incorrect! Try again.")
        input(f"Square root of pi: {sqrt}")
        system("cls")
