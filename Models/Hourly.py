from Models.Employee import Employee


class Hourly(Employee):
    _hourly_salary: float

    def __init__(self, name, address, id_number):
        super().__init__(name, address, id_number)
        self._type = "Horista"
        self._hourly_salary = float(input("Informe a hora de trabalho do funcionário: R$ "))

    @property
    def hourly_salary(self):
        return self._hourly_salary

    @hourly_salary.setter
    def hourly_salary(self, hourly_salary):
        self._hourly_salary = hourly_salary
