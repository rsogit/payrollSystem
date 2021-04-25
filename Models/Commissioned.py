from Models.Employee import Employee
from Models.Sale import Sale


class Commissioned(Employee):
    _salary: float
    _percentage: float
    _sales: [Sale]

    def __init__(self, name, address, id_number):
        super().__init__(name, address, id_number)
        self._type = "Comissionado"
        self._sales = []
        self._salary = float(input("Informe o salário do funcionário: R$ "))
        self._percentage = float(input("Informe a porcentagem de comissão do funcionário (apenas números): "))

    def __init__(self, name, address, id_number, salary, percentage):
        super().__init__(name, address, id_number)
        self._type = "Comissionado"
        self._sales = []
        self._salary = float(salary)
        self._percentage = float(percentage)

    def add_sale(self, sale):
        self._sales.append(sale)

    def print_sales(self):
        for (index, sale) in enumerate(self._sales):
            print(f'{index+1} - Data da venda: {sale.date} - Valor: R$ {sale.value}')

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