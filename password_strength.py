import getpass
import os
import string
import sys


def main():
    file_path = None
    if len(sys.argv) == 2:
        file_path = sys.argv[1]

    elif len(sys.argv) > 2:
        exit('Try again with right format "$ python password_strength.py" or '
             '"$ python password_strength.py <path to file with '
             'common passwords>"')

    password = get_user_password()
    password_strength = get_password_strength(password)
    print('The strength of your password: {}'.format(password_strength))

    if file_path:
        most_common_passwords = load_most_common_passwords(file_path)
        password_in_most_common_passwords = check_strings_for_occurrence(
            password,
            most_common_passwords)

        if password_in_most_common_passwords:
            print('Your password included in most common passwords list.')
        else:
            print('Your password does not included '
                  'in most common passwords list.')


def get_user_password():
    password = getpass.getpass("Please enter your password for check "
                               "and press Enter:")
    assert password != '', 'Password should not be empty string.'
    return password


def get_password_strength(password: str):
    characteristic_counter = 0
    password_strength_coefficient = get_password_strength_coefficient(password)

    password_characteristics = {
        'password_contains_digits': check_strings_for_occurrence(
            password,
            string.digits),
        'password_contains_upper_case ': check_strings_for_occurrence(
            password,
            string.ascii_uppercase),
        'password_contains_lower_case ': check_strings_for_occurrence(
            password,
            string.ascii_lowercase),
        'password_contains_punctuation ': check_strings_for_occurrence(
            password,
            string.punctuation)}
    for characteristic in password_characteristics:
        characteristic_counter += password_characteristics[characteristic]/2
        # divide 2 because each True should be equal 0,5
        # 0,5 is a unit of counter

    strength_counter = characteristic_counter * password_strength_coefficient

    return strength_counter


def get_password_strength_coefficient(password: str):
    max_coefficient = 5
    password_len = len(password)
    password_strength_coefficient = (password_len + (-password_len % 2)) // 2
    if password_strength_coefficient > max_coefficient:
        password_strength_coefficient = max_coefficient

    return password_strength_coefficient


def load_most_common_passwords(file_path: str):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as file:
        return file.read()


def check_strings_for_occurrence(string_1: str,
                                 string_2: str):
    assert type(string_1) == str, 'Type of parameter is not a string'
    assert type(string_2) == str, 'Type of parameter is not a string'
    intersection_list = set(string_1).intersection(string_2)

    return bool(intersection_list)


if __name__ == "__main__":
    main()
