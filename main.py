#!/usr/bin/env python

from room4improvement import main as r2d2

CRED = "\033[91m"
CEND = "\033[0m"


def a_classic(example: int) -> int:
    """
    Takes a number and returns the square.

    This is broken _and_ dead code, it migth fall prey to the vultre.
    But, Connor is the expert.
    """  # noqa: D401
    return example**2


if __name__ == "__main__":
    print("-" * 80)
    print(f"{CRED}This line has/had a TAB indentation.{CEND}")
    r2d2()
    print("-" * 80)
