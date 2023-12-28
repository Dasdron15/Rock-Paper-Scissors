import random

# Lists

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_symbols = ["!", "@", "#", "$", "%", "-"]
ending = []

# Functions


def list_to_string(ending):
    first_string = ""
    return first_string.join(ending)


def generating_system():
    if contain_upper_letters == "y" or contain_upper_letters == "yes" and contain_numbers == "y" or contain_numbers == "yes" and contain_symbols == "y" or contain_symbols == "yes":
        all_included()
    elif contain_numbers == "y" or contain_numbers == "yes" and contain_symbols == "y" or contain_symbols == "yes":
        nums_and_symbols()
    elif contain_numbers == "y" or contain_numbers == "yes" and contain_upper_letters == "y" or contain_upper_letters == "yes":
        numbers_and_up_letters()
    elif contain_upper_letters == "y" or contain_upper_letters == "yes":
        only_up_letters()
    elif contain_numbers == "y" or contain_numbers == "yes":
        only_numbers()
    elif contain_symbols == "y" or contain_symbols == "yes":
        only_symbols()


def all_included():
    for i in range(random.randint(1, 3)):
        nums_in_pass = random.choice(numbers)
        ending.append(nums_in_pass)
    for e in range(random.randint(1, 6)):
        letters_in_pass = random.choice(lower_letters)
        ending.append(letters_in_pass)
    for o in range(random.randint(1, 6)):
        upper_in_pass = random.choice(upper_letters)
        ending.append(upper_in_pass)
    for f in range(random.randint(1, 3)):
        symbols_in_pass = random.choice(special_symbols)
        ending.append(symbols_in_pass)
    random.shuffle(ending)


def nums_and_symbols():
    for i in range(random.randint(1, 3)):
        nums_in_pass = random.choice(numbers)
        ending.append(nums_in_pass)
    for e in range(random.randint(1, 6)):
        letters_in_pass = random.choice(lower_letters)
        ending.append(letters_in_pass)
    for o in range(random.randint(1, 3)):
        symbols_in_pass = random.choice(special_symbols)
        ending.append(symbols_in_pass)
    random.shuffle(ending)


def numbers_and_up_letters():
    for i in range(random.randint(1, 3)):
        nums_in_pass = random.choice(numbers)
        ending.append(nums_in_pass)
    for e in range(random.randint(1, 6)):
        letters_in_pass = random.choice(lower_letters)
        ending.append(letters_in_pass)
    for o in range(random.randint(1, 6)):
        upper_in_pass = random.choice(upper_letters)
        ending.append(upper_in_pass)
    random.shuffle(ending)


def only_up_letters():
    for i in range(random.randint(1, 6)):
        letters_in_pass = random.choice(lower_letters)
        ending.append(letters_in_pass)
    for e in range(random.randint(1, 6)):
        upper_in_pass = random.choice(upper_letters)
        ending.append(upper_in_pass)
    random.shuffle(ending)


def only_numbers():
    for i in range(random.randint(1, 6)):
        letters_in_pass = random.choice(lower_letters)
        ending.append(letters_in_pass)
    for e in range(random.randint(1, 3)):
        numbers_in_pass = random.choice(numbers)
        ending.append(numbers_in_pass)
    random.shuffle(ending)


def only_symbols():
    for i in range(random.randint(1, 6)):
        letters_in_pass = random.choice(lower_letters)
        ending.append(letters_in_pass)
    for e in range(random.randint(1, 3)):
        symbols_in_pass = random.choice(special_symbols)
        ending.append(symbols_in_pass)
    random.shuffle(ending)


# Inputs

digit_number = int(input("How many digits will your password contain?: "))
contain_upper_letters = input("Will your password contain upper case letters? (Y/N): ")
contain_numbers = input("Will your password contain numbers? (Y/N): ")
contain_symbols = input("Will your password contain special symbols? (Y/N): ")
contain_upper_letters = contain_upper_letters.lower()
contain_symbols = contain_symbols.lower()
contain_numbers = contain_numbers.lower()

generating_system()


print("")
print("Here are your passwords:")
for k in range(5):
    result = list_to_string(ending)
    how_many_digits = len(result)
    if how_many_digits > digit_number:
        equal = how_many_digits - digit_number
        for i in range(equal):
            result = result.rstrip(result[-1])
    elif how_many_digits < digit_number:
        generating_system()
        if how_many_digits > digit_number:
            equal = how_many_digits - digit_number
            for i in range(equal):
                result = result.rstrip(result[-1])
    elif how_many_digits == digit_number:
        print()
    print(result)
    ending = []
    generating_system()