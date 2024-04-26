def missing_type(number):
    if number is None:
        raise TypeError('Number cannot be None')
    print(f"got -> {number:>8} and it's type is {type(number)}")

def print_integer(number: int) -> None:
    if number is None:
        raise TypeError('Number cannot be None')
    print(f"got -> {number:>8} and it's type is {type(number)}")

def camelCase(string):
    """the function should not be using camelCase"""
    print(f"got a {string} and it's type is {type(string)}")
def main():
    """"""
    print("Welcome to the best linting example ever")
    try:
        missing_type(42)
        missing_type(3.14)
        missing_type()
    except TypeError as e:
        print(f"well, that was stupid: {e}")

    print_integer(3.14)

if __name__ == '__main__':
    main()