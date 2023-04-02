from random import sample


def generate_lotto_numbers():
    """Generate 6 random numbers
    :return: list[int] - sorted list of 6 numbers
    """
    return sorted(sample(range(1, 50), 6))


def get_user_numbers():
    """User inputs 6 unique numbers from 1 to 49
    :return: list[int] - sorted list of 6 numbers
    """
    user_numbers = []

    while len(user_numbers) < 6:
        try:
            number = int(input('Enter numbers from 1 to 49: '))
            if number < 1 or number > 49:
                raise ValueError('Number out of range')    #Checking range
            elif number in user_numbers:
                raise ValueError("You can't pick the same number twice!")    #Checking repetitions
            else:
                user_numbers.append(number)
        except ValueError as err:
            print(err)
    return sorted(user_numbers)


def play_lotto():
    """Takes player and lotto numbers and compares them
    :return: f string - text message
    """
    lotto_numbers = generate_lotto_numbers()
    user = get_user_numbers()

    matched_numbers = sum([1 for number in user if number in lotto_numbers])    #Compares user and computer numbers
    return f'Your matched {matched_numbers} numbers, lotto numbers: {lotto_numbers}'


print(play_lotto())
