import re


def get_password_strength(password):
    checklist = []

    # length
    if len(password) > 5:
        checklist.append(1)
    else:
        checklist.append(0)

    # the use of both upper-case and lower-case letters (case sensitivity)
    if re.search('[A-Z]', password) and re.search('[a-z]', password):
        checklist.append(1)
    else:
        checklist.append(0)

    # inclusion of one or more numerical digits
    if re.search('[\d]', password):
        checklist.append(1)
    else:
        checklist.append(0)

    # inclusion of special characters, such as @, #, $
    if re.search('[@#$]', password):
        checklist.append(1)
    else:
        checklist.append(0)

    # prohibition of words found in a password blacklist
    if not any(substring in password.lower() for substring in password_blacklist):
        checklist.append(1)
    else:
        checklist.append(0)

    # prohibition of words found in the user's personal information
    words_list = user_personal_info.lower().split()
    if not any(substring in password.lower() for substring in words_list):
        checklist.append(1)
    else:
        checklist.append(0)

    # prohibition of use of company name or an abbreviation
    if not company.lower() in password:
        checklist.append(1)
    else:
        checklist.append(0)

    company_splitted = company.split()
    if len(company_splitted) > 1:
        abbreviation = ''.join(word[0] for word in company_splitted)
        if not abbreviation.lower() in password:
            checklist.append(1)
        else:
            checklist.append(0)

    # prohibition of passwords that match the format of calendar dates,
    # license plate numbers, telephone numbers, or other common numbers
    if not re.fullmatch('\d\d/\d\d/\d{4}', password) \
            or re.fullmatch('\d{4}/\d\d/\d\d', password) \
            or re.fullmatch('\d\d-\d\d-\d{4}', password) \
            or re.fullmatch('\d{4}-\d\d-\d\d', password) \
            or re.search('\d{3}-\d\d-\d\d', password) \
            or re.fullmatch('[a-zA-Z]\d{3}[a-zA-Z]{2}\d{2,3}', password):
        checklist.append(1)
    else:
        checklist.append(0)

    password_strength = round(10*sum(checklist)/len(checklist))

    return password_strength


def main():
    password = input('Input password: ')
    print('Password complexity: ', get_password_strength(password))


if __name__ == '__main__':
    password_blacklist = ['password', 'pwd', 'parol']
    user_personal_info = 'Ivanov Ivan Inanovich, born 21.12.1975 in Moscow'
    company = 'General motors'
    main()
