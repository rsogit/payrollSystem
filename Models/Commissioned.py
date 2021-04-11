from Models.Employee import Employee


class Commissioned(Employee):
    _salary: float
    _percentage: float

    def __init__(self, name, address, id_number):
        super().__init__(name, address, id_number)
        self._type = "Comissionado"
        self._salary = float(input("Informe o salário do funcionário: R$ "))
        self._percentage = float(input("Informe a porcentagem de comissão do funcionário (apenas números): "))

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            print("O salário informado está incorreto.")

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        if percentage >= 0:
            self._percentage = percentage
        else:
            print("A porcentagem informada está incorreta.")
