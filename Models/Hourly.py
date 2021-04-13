from Models.Employee import Employee
from Models.TimeCard import TimeCard


class Hourly(Employee):
    _hourly_salary: float
    _time_cards: [TimeCard]

    def __init__(self, name, address, id_number):
        super().__init__(name, address, id_number)
        self._type = "Horista"
        self._time_cards = []
        self._hourly_salary = float(input("Informe a hora de trabalho do funcionário: R$ "))

    def __init__(self, name, address, id_number, hourly_salary):
        super().__init__(name, address, id_number)
        self._type = "Horista"
        self._time_cards = []
        self._hourly_salary = float(hourly_salary)

    def add_timecard(self, timecard):
        self._time_cards.append(timecard)

    def print_timecards(self):
        for (index, time_card) in enumerate(self._time_cards):
            print(f'{index+1} - Horas trabalhadas: {time_card.work_hours}hrs')

    @property
    def time_cards(self):
        return self._time_cards

    @property
    def hourly_salary(self):
        return self._hourly_salary

    @hourly_salary.setter
    def hourly_salary(self, hourly_salary):
        self._hourly_salary = hourly_salary
