from application.db.people import Employee # задание 1
from application.salary import calculate_salary

from datetime import datetime

import pygame # задание 4, файл requirements.txt


if __name__ == '__main__': # задание 2
    current_date = datetime.today() # задание 3
    print(current_date)

    employee = Employee('Olya', 40, 1500)
    hours, rate = employee.get_employees_details('Olya')
    salary = calculate_salary(hours, rate)
    print(f"Зарплата у {employee.name}: {salary} в неделю.")