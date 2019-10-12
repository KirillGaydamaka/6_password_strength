import argparse
import re
import string
import getpass


def check_password_length(password, minimal_length):
    if len(password) > 2*minimal_length:
        return 2
    return len(password) > minimal_length


def check_case_sensitivity(password):
    return bool(re.search('[A-Z]', password) and re.search('[a-z]', password))


def check_for_digits(password):
    return bool(re.search(r'[\d]', password))


def check_for_special(password):
    return bool(re.search('[{}]'.format(string.punctuation), password))


def check_for_blacklisted(password, password_blacklist):
    blacklisted = password.lower() in password_blacklist
    return not blacklisted


def check_for_personal_info(password, user_personal_info):
    words_list = user_personal_info.lower().split()
    contain_personal_info = any(substring in
                                password.lower() for substring in words_list)
    return not contain_personal_info


def check_for_company_name(password, company):
    return not company.lower() in password


def check_for_company_abbreviation(password, company):
    company_splitted = company.split()
    abbreviation = ''.join(word[0] for word in company_splitted)
    return len(company_splitted) > 1 and not abbreviation.lower() in password


def check_for_numbers(password):
    return any((re.fullmatch(r'\d\d/\d\d/\d{4}', password),
                re.fullmatch(r'\d{4}/\d\d/\d\d', password),
                re.fullmatch(r'\d\d-\d\d-\d{4}', password),
                re.fullmatch(r'\d{4}-\d\d-\d\d', password),
                re.search(r'\d{3}-\d\d-\d\d', password),
                re.fullmatch(r'[a-zA-Z]\d{3}[a-zA-Z]{2}\d{2,3}', password)))


def create_parser():
    parser = argparse.ArgumentParser(description='Parameters')

    parser.add_argument('password_blacklist_filepath', nargs=1,
                        help='Password blacklist file path')

    parser.add_argument('minimal_length', nargs=1, type=int,
                        default=5, help='Minimal password length')

    parser.add_argument('user_info_filepath', nargs=1,
                        help='User info file path')

    args = parser.parse_args()
    return args


def load_password_blacklist(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        blacklist = file.read().splitlines()
        return blacklist


def load_user_info(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        company, user_personal_info = file.read().splitlines()
        return company, user_personal_info


def get_password_strength(password, password_blacklist, minimal_length,
                          user_personal_info, company):
    return sum([check_password_length(password, minimal_length),
                check_case_sensitivity(password),
                check_for_digits(password),
                check_for_special(password),
                check_for_blacklisted(password, password_blacklist),
                check_for_personal_info(password, user_personal_info),
                check_for_company_name(password, company),
                check_for_company_abbreviation(password, company),
                check_for_numbers(password)])


def main():
    try:
        parser = create_parser()
        blacklist_fpath = parser.password_blacklist_filepath
        blacklist = load_password_blacklist(blacklist_fpath[0])
        minimal_length = parser.minimal_length[0]
        user_info_filepath = parser.user_info_filepath
        company, user_personal_info = load_user_info(user_info_filepath[0])
        password = getpass.getpass()
        print('Password complexity: ',
              get_password_strength(password,
                                    blacklist,
                                    minimal_length,
                                    user_personal_info,
                                    company))
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    main()
