from datetime import datetime

from application.salary import *
from application.db.people import *


def show_current_date():
    print(f"Текущая дата: {datetime.now().strftime('%d.%m.%Y')}")


if __name__ == '__main__':
    show_current_date()
    calculate_salary()

    show_current_date()
    get_employees()
