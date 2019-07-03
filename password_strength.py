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
             '"$ python password_strength.py <path to file with common passwords>"')

    password = get_user_password()
    print('The strength of your password: {}'.format(get_password_strength(password)))

    if file_path:
        password_in_most_common_passwords = check_word_in_most_common_password_list(password,
                                                                                    file_path)

        if password_in_most_common_passwords:
            print('Your password included in most common passwords list.')
        else:
            print('Your password does not included in most common passwords list.')


def get_user_password():
    attempts_limit = 15

    for _ in range(attempts_limit):
        password = getpass.getpass("Please enter your password for check and press Enter:")
        if password != '':
            return password
        else:
            print('Password should not be empty string.')

    print('Number of attempts exceeded. Try to restart the script.')


def get_password_strength(password: str):
    strength_counter = 0
    password_strength_coefficient = get_password_strength_coefficient(password)
    password_characteristics = {
        'password_contains_digits': check_strings_for_occurrence(password, string.digits),
        'password_contains_upper_case ': check_strings_for_occurrence(password,
                                                                      string.ascii_uppercase),
        'password_contains_lower_case ': check_strings_for_occurrence(password,
                                                                      string.ascii_lowercase),
        'password_contains_punctuation ': check_strings_for_occurrence(password,
                                                                       string.punctuation)}
    for characteristic in password_characteristics:
        strength_counter = strength_counter + password_characteristics[characteristic]

    final_strength_counter = (strength_counter / 2) * password_strength_coefficient

    return final_strength_counter


def get_password_strength_coefficient(password: str):
    password_len = len(password)
    password_strength_coefficient = (password_len + (-password_len % 2)) // 2

    if password_strength_coefficient > 5:
        password_strength_coefficient = 5

    return password_strength_coefficient


def check_word_in_most_common_password_list(word: str,
                                            file_path: str):
    most_common_passwords = load_list_of_common_password_data(file_path)
    assert most_common_passwords is not None, 'No file in path'
    return bool(word in most_common_passwords)


def load_list_of_common_password_data(file_path: str):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as file:
        return file.read()


def check_strings_for_occurrence(string_1: str,
                                 string_2: str):
    assert type(string_1) == str and type(string_2) == str, 'Type of parameter is not a string'
    intersection_list = set(string_1).intersection(string_2)

    return bool(intersection_list)


if __name__ == "__main__":
    main()
