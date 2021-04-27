from Models.Employee import Employee
from Models.Sale import Sale
from datetime import date
import pandas as pd


class Commissioned(Employee):
    _salary: float
    _percentage: float
    _sales: [Sale]

    def __init__(self, name, address, id_number, salary=None, percentage=None, schedule_type="weekly 2 friday"):
        super().__init__(name, address, id_number, schedule_type)
        self._type = "Comissionado"
        self._sales = []
        if salary:
            self._salary = salary
        else:
            self._salary = float(input("Informe o salário do funcionário: R$ "))
        if percentage:
            self._percentage = percentage
        else:
            self._percentage = float(input("Informe a porcentagem de comissão do funcionário (apenas números): "))

    def add_sale(self):
        date = input("Insira a data da venda no formato DD/MM/AAAA. \nEx.: 08/04/2021\n")
        value = input("Digite o valor da venda: \nR$ ")
        sale_result = Sale(date, value)
        self._sales.append(sale_result)
        self.print_sales()

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
