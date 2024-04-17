from application import salary
from application.db import people
from datetime import datetime
from colorama import Fore, Back, Style


if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    print(Fore.GREEN + str(datetime.now()))
    print(Fore.GREEN + 'green text')
    print(Back.YELLOW + 'yellow back')
    print(Style.BRIGHT + 'bright' + Style.RESET_ALL)