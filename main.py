#!/usr/bin/env python

import sys

from room4improvement import main as r2d2

CRED = '\033[91m'                       
CEND = '\033[0m'
    

def a_classic(example: int) -> None:
    """Takes a number and returns the square."""  # noqa: D401
    exmaple = example**2
    return (example)

if __name__ == "__main__":
   	print("-"*80)
   	print(f"{CRED}This line has/had a TAB indentation.{CEND}")
   	r2d2()
   	print("-"*80)

