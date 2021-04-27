from Models.Employee import Employee
from Models.TimeCard import TimeCard


class Hourly(Employee):
    _hourly_salary: float
    _time_cards: [TimeCard]

    def __init__(self, name, address, id_number, hourly_salary=None, schedule_type="weekly 1 friday"):
        super().__init__(name, address, id_number, schedule_type)
        self._type = "Horista"
        self._time_cards = []
        if hourly_salary:
            self._hourly_salary = hourly_salary
        else:
            self._hourly_salary = float(input("Informe a hora de trabalho do funcionário: R$ "))

    def pay_salary(self):
        max_hours = 8
        total_hours = 0
        brute_salary = 0
        for timecard in self._time_cards:
            day_hours = timecard.work_hours.seconds / 3600
            if day_hours > max_hours:
                bonus_hours = (day_hours - max_hours)
                bonus_salary = bonus_hours * self._hourly_salary * 1.5
                total_hours = total_hours + day_hours
                brute_salary = total_hours * self._hourly_salary + bonus_salary
            else:
                total_hours = total_hours + day_hours
                brute_salary = total_hours * self._hourly_salary
        print(f'Salário Bruto = R$ {brute_salary}')
        liquid_salary = brute_salary
        if self.union_info.is_active:
            total_service_fee = 0
            if len(self.union_info.service_taxes) > 0:
                for service_fee in self.union_info.service_taxes:
                    total_service_fee = total_service_fee + service_fee.value
            liquid_salary = liquid_salary - self.union_info.monthly_tax - total_service_fee
            print(f'Salário Líquido = R$ {liquid_salary}')
        return liquid_salary


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
