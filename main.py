#!/usr/bin/env python

import sys


def missing_type(number):
    if number is None:
        raise TypeError
    print(f"got -> {number:>8} and it's type is {type(number)}")


def print_integer(number: int) -> None:
    """Print a number and its type."""
    if number is None:
        raise TypeError
    print(f"got -> {number:>8} and it's type is {type(number)}")


def camelCase(string: str) -> None:
    """Print the received string and the type of the received string."""
    print(f"got a {string} and it's type is {type(string)}")


def capital_variable(number: int) -> float:
    """
    The function should not be using capitalized variables.

    2nd line
    """  # noqa: D401
    B = number * 3.14
    return B * 2.72


def two_spaces(number: int) -> float:
  print(f"got a {number} and it's type is {type(number)}")


def a_very_long_line() -> None:
    """A very long line."""  # noqa: D401
    print(
        "This is a very long line, and the linter should complain about the lenght of the line. It is now 125 chars long",
    )


def main() -> None:
    """Main."""  # noqa: D401
    print("Welcome to the best linting example ever")
    try:
        missing_type(42)
        missing_type(3.14)
        missing_type()
    except TypeError as e:
        print(f"well, that was stupid: {e}", file=sys.stderr)

    print_integer(3.14)


if __name__ == "__main__":
    main()
