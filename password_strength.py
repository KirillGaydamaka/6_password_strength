import re
import getpass

def check_password_length(password):
    if len(password) > mininmal_length:
        return 1
    if len(password) > 2*mininmal_length:
        return 2

def check_case_sensitivity(password):
    return bool(re.search('[A-Z]', password) and re.search('[a-z]', password))

def check_for_digits(password):
    return bool(re.search('[\d]', password))

def check_for_special(password): # допилить
    return bool(re.search('[@#$]', password))

def check_for_not_blacklisted(password):
    blacklisted = any(substring in
                      password.lower() for substring in password_blacklist)
    return not blacklisted

def check_for_personal_info(password):
    words_list = user_personal_info.lower().split()
    contain_personal_info = any(substring in
                                password.lower() for substring in words_list)
    return not contain_personal_info

def check_for_company_name(password):
    return not company.lower() in password

def check_for_company_abbreviation(password):
    company_splitted = company.split()
    abbreviation = ''.join(word[0] for word in company_splitted)
    return len(company_splitted) > 1 and not abbreviation.lower() in password

def check_for_numbers(password):
    if re.fullmatch('\d\d/\d\d/\d{4}', password) \
            or re.fullmatch('\d{4}/\d\d/\d\d', password) \
            or re.fullmatch('\d\d-\d\d-\d{4}', password) \
            or re.fullmatch('\d{4}-\d\d-\d\d', password) \
            or re.search('\d{3}-\d\d-\d\d', password) \
            or re.fullmatch('[a-zA-Z]\d{3}[a-zA-Z]{2}\d{2,3}', password):
        return False
    return True

def get_password_strength(password):
    password_strength = 0
    password_strength += check_password_length(password)
    password_strength += check_case_sensitivity(password)
    password_strength += check_for_digits(password)
    password_strength += check_for_special(password)
    password_strength += check_for_not_blacklisted(password)
    password_strength += check_for_personal_info(password)
    password_strength += check_for_company_name(password)
    password_strength += check_for_company_abbreviation(password)
    password_strength += check_for_numbers(password)
    return password_strength


def main():
    password = input('Input password: ')
    #password = getpass.getpass()
    print('Password complexity: ', get_password_strength(password))


if __name__ == '__main__':
    password_blacklist = ['password', 'pwd', 'parol']
    mininmal_length = 5
    user_personal_info = 'Ivanov Ivan Inanovich, born 21.12.1975 in Moscow'
    company = 'General motors'
    main()
