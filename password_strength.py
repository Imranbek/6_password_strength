import gc
import os
import string


def main():
    password = get_user_password()
    print('\nThe strength of your password: {}'.format(get_password_strength(password)))
    gc.collect()


def get_user_password():
    print('Please enter your password for check and press Enter')
    attempts_limit = 15

    for _ in range(attempts_limit):
        password = input()
        if password != '' and password is not None:
            return password
        else:
            print('Password should not be equal empty string')

    print('Number of attempts exceeded. Try to restart the script.')


def load_list_of_command_password_data():
    file_path = '10-million-passwords.txt'
    if not os.path.exists(file_path):
        return None
    with open(file_path, "r") as file:
        return file.read()


def get_password_strength(password: str):
    strength_counter = 0
    password_characteristics = {'password_contains_digits': check_strings_for_occurrence(password, string.digits),
                                'password_contains_upper_case ': check_strings_for_occurrence(password, string.ascii_uppercase),
                                'password_contains_lower_case ': check_strings_for_occurrence(password, string.ascii_lowercase),
                                'password_contains_punctuation ': check_strings_for_occurrence(password, string.punctuation)}
    for key, flag in password_characteristics.items():
        strength_counter = strength_counter + 1 if flag is True else strength_counter
    password_not_in_most_common_passwords = check_word_not_in_most_common_password_list(password)
    if password_not_in_most_common_passwords is True:
        strength_counter = strength_counter + 6
    gc.collect()

    return strength_counter


def check_word_not_in_most_common_password_list(word):
    most_common_password_list = load_list_of_command_password_data()
    gc.collect()
    if word in most_common_password_list:
        return False
    else:
        return True


def check_strings_for_occurrence(string_1: str,
                                 string_2: str):
    assert type(string_1) == str and type(string_2) == str, 'Type of parameter is not a string'
    diff_list = [x for x in list(string_1) if x in list(string_2)]
    if diff_list:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
