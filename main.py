from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees


def show_current_date():
    print(f"Текущая дата: {datetime.now().strftime('%d.%m.%Y')}")


if __name__ == '__main__':
    show_current_date()
    calculate_salary()

    show_current_date()
    get_employees()
