#!/usr/bin/env python


def capitalVariable(number):
    """
    The function should not be using capitalized variables.
    """
    if number is None:
      raise TypeError
    print(f"got -> {number:>8} and it's type is {type(number)}")

    print(
        "This is a very long line, and the linter should complain about the lenght of the line. It is now 125 chars long",
    )

    B = number * 3.14
    return B * 2.72


def main() -> None:
    """Main."""
    print("Welcome to the best linting example ever")
    try:
        capitalVariable(3.14)
        capitalVariable()
    except TypeError as e:
        print(f"well, that was stupid: {e}")



if __name__ == "__main__":
    main()
