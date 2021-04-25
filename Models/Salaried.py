from Models.Employee import Employee


class Salaried(Employee):
    _salary: float

    def __init__(self, name, address, id_number, salary=None):
        super().__init__(name, address, id_number)
        self._type = "Assalariado"
        if salary:
            self._salary = float(salary)
        else:
            self._salary = float(input("Informe o salário do funcionário: R$ "))

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            print("O salário informado está incorreto.")