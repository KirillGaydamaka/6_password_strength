# Password Strength Calculator

The script calculates password strength. It takes passoword from user input.
User info and password blacklist are set as global variables.

The script needs Python 3.5 interpreter.

Example of script launch on Linux, Python 3.5:

```bash
$ python password_strength.py <password_blacklist_filepath> <minimal_length> <user_info_filepath>
```
password_blacklist_filepath - path to the file with passwords blacklist. You can take a list of blacklisted passwords here: https://github.com/danielmiessler/SecLists/tree/master/Passwords.
Default name: password_blacklist.txt. Each blacklisted password on new line.

minimal_length - minimal length of the password (default is 5). If the password is shorter, password strength is decreased.

user_info_filepath - path to the file with information about user. Default name: user_info.txt. First line in the file is user's company name, second line - user's personal information.

Example of script work:

```bash
Input password: A12DF4#$
Password complexity:  9

Process finished with exit code 0
```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
