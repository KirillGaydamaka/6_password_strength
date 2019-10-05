import re


def get_password_strength(password):
    password_strength = 0

    # length
    password_strength += len(password) > mininmal_length
    password_strength += len(password) > 2*mininmal_length

    # the use of both upper-case and lower-case letters (case sensitivity)
    password_strength += bool(re.search('[A-Z]', password) and re.search('[a-z]', password))

    # inclusion of one or more numerical digits
    password_strength += bool(re.search('[\d]', password))

    # inclusion of special characters, such as @, #, $
    password_strength += bool(re.search('[@#$]', password))

    # prohibition of words found in a password blacklist
    password_strength += not any(substring in password.lower() for substring in password_blacklist)

    # prohibition of words found in the user's personal information
    words_list = user_personal_info.lower().split()
    password_strength += not any(substring in password.lower() for substring in words_list)

    # prohibition of use of company name or an abbreviation
    password_strength += not company.lower() in password

    company_splitted = company.split()
    abbreviation = ''.join(word[0] for word in company_splitted)
    password_strength += len(company_splitted) > 1 and not abbreviation.lower() in password

    # prohibition of passwords that match the format of calendar dates,
    # license plate numbers, telephone numbers, or other common numbers
    password_strength += check_for_numbers(password)

    return password_strength


def check_for_numbers(password):
    if re.fullmatch('\d\d/\d\d/\d{4}', password) \
            or re.fullmatch('\d{4}/\d\d/\d\d', password) \
            or re.fullmatch('\d\d-\d\d-\d{4}', password) \
            or re.fullmatch('\d{4}-\d\d-\d\d', password) \
            or re.search('\d{3}-\d\d-\d\d', password) \
            or re.fullmatch('[a-zA-Z]\d{3}[a-zA-Z]{2}\d{2,3}', password):
        return False
    return True

def main():
    password = input('Input password: ')
    print('Password complexity: ', get_password_strength(password))


if __name__ == '__main__':
    password_blacklist = ['password', 'pwd', 'parol']
    mininmal_length = 5
    user_personal_info = 'Ivanov Ivan Inanovich, born 21.12.1975 in Moscow'
    company = 'General motors'
    main()
