#!/usr/bin/env python

from typing import Any


def capital_variable(number: Any) -> float:  # noqa: ANN401
    """ """  # noqa: D419
    if number is None:
        raise TypeError
    print(f"got -> {number:>8} and it's type is {type(number)}")

    print(
        "This is a very long line, and the linter should complain about the lenght of the line. It is now 125 chars long",  # noqa: E501
    )

    b = number * 3.14
    return b * 2.72


def main() -> None:
    """Main."""  # noqa: D401
    print("Welcome to the best linting example ever")
    try:
        capital_variable(3.14)
        # capital_variable()  # noqa: ERA001
    except TypeError as e:
        print(f"well, that was stupid: {e}")


if __name__ == "__main__":
    main()
