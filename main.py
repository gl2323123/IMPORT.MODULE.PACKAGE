from Aplication.db.people import get_employees
from Aplication.salary import calculate_salary
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    get_employees()
    calculate_salary()