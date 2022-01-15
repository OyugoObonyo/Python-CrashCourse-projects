import random

"""
Module that generates a random password string
password should be at least 8 characters long with at least
2 uppercase letters, 2 numbers and 2 allowed symbols
"""


def generate_password():
    # Store allowed symbols, numbers and letters in lists
    allowed_symbols = [
        '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '()', '_', '-', '+',
        '=', '{', '[', '}', ']', '|', '\\', ':', ';', '"', "'", '<', '>', '.',
        '?', '/']
    allowed_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    allowed_letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z'
    ]

    # Get user's desired number of symbols, letters and nums in the password
    num_symbols = int(input('How many symbols would you like in your password?'))
    if num_symbols > len(allowed_symbols):
        return (print(f"You can only pick up to {len(allowed_symbols)} symbols"))
    elif num_symbols < 2:
        return (print(f"You can pick a minimum of 2 symbols"))
        
    num_numbers = int(input('How many numbers would you like in your password?'))
    if num_numbers > len(allowed_numbers):
        return (print(f"You can only pick up to {len(allowed_numbers)} numbers"))
    elif num_symbols < 2:
        return (print(f"You can pick a minimum of 2 symbols"))

    num_letters = int(input('How many letters would you like in your password?'))
    if num_letters > len(allowed_letters):
        return (print(f"You can only pick up to {len(allowed_symbols)} letters"))
    elif num_symbols < 2:
        return (print(f"You can pick a minimum of 2 symbols"))

    # Extract specified elements from each list
    sym_list = random.sample(allowed_symbols, num_symbols)
    num_list = random.sample(allowed_numbers, num_numbers)
    lett_list = random.sample(allowed_letters, num_letters)

    # Concatenate extracted elements
    password = sym_list + num_list + lett_list
    random.shuffle(password)
    password = "".join(map(str, password))
    return password


if __name__ == '__main__':
    password = generate_password()
    print(f"Here is your password: ")