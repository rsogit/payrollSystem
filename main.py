# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import datetime
import time

from Models.TimeCard import TimeCard
from Models.Sale import Sale
from Models.Hourly import Hourly
from Models.Salaried import Salaried
from Models.Commissioned import Commissioned

id_counting: int = 1


def show_menu():
    print("=======Sistema de Folha de Pagamento========\n")
    print("MENU PRINCIPAL\n")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Remover Funcionário")
    print("4 - Adicionar cartão de ponto para um funcionário")
    print("5 - Adicionar Resultado de Venda para um funcionário")

    print("6 - Sair\n")


def add_timecard(employee):

    time_in = input("Digite o horário de entrada no formato HH:MM. \nEx.: '08:00'\n").split(":")
    date_time_in = datetime.time(int(time_in[0]), int(time_in[1]))
    time_out = input("Digite o horário de saída no formato HH:MM. \nEx.: '12:00'\n").split(":")
    date_time_out = datetime.time(int(time_out[0]), int(time_out[1]))

    if date_time_out >= date_time_in:
        work_hours = int(time_out[0]) - int(time_in[0])
        timecard = TimeCard(date_time_in, date_time_out, work_hours)
        employee.add_timecard(timecard)
    else:
        print("O horário informado é inválido")


def add_sale(employee):
    date = input("Insira a data da venda no formato DD/MM/AAAA. \nEx.: 08/04/2021\n")
    value = input("Digite o valor da venda: \nR$ ")
    sale_result = Sale(date, value)
    employee.add_sale(sale_result)
    employee.print_sales()


def open_seed_file():

    global id_counting

    with open('Utils/data.json') as json_file:
        data = json.load(json_file)['employees']

    for employee in data:
        if employee['type'] == "Horista":
            employee = Hourly(employee['name'], employee['address'], id_counting, employee['salary'])
        elif employee['type'] == "Assalariado":
            employee = Salaried(employee['name'], employee['address'], id_counting, employee['salary'])
        elif employee['type'] == "Comissionado":
            employee = Commissioned(employee['name'], employee['address'], id_counting, employee['salary'],
                                    employee['percentage'])
        else:
            print("Falha no cadastro do novo funcionário, por favor tente novamente respondendo o tipo de 1 a 3.")
            return
        id_counting = id_counting + 1
        employees.append(employee)
        print(f'Total de funcionários: {len(employees)}')


def add_employee():

    global id_counting

    name = input("Insira o nome do funcionário: ")
    address = input("Insira o endereço do funcionário: ")

    print("Selecione o número correspondente ao tipo de funcionário: ")
    employee_type = int(input("1. Horista\n2. Assalariado\n3. Comissionado\n"))

    if employee_type == 1:
        employee = Hourly(name, address, id_counting)
    elif employee_type == 2:
        employee = Salaried(name, address, id_counting)
    elif employee_type == 3:
        employee = Commissioned(name, address, id_counting)
    else:
        print("Falha no cadastro do novo funcionário, por favor tente novamente respondendo o tipo de 1 a 3.")
        return
    id_counting = id_counting + 1
    employees.append(employee)
    print(f'Total de funcionários: {len(employees)}')
    print("Novo funcionário adicionado com sucesso!\n")


def delete_employee(size):
    if size != 0:
        print("Digite o número do funcionário que deseja deletar: ")
        show_all_employees(employees)
        employee_number = int(input("\n"))
        for index, employee in enumerate(employees):
            if employee.id_number == employee_number:
                deleted_employee = employees.pop(index)
                print(f'Funcionário "{deleted_employee.name}" deletado com sucesso!')


def show_all_employees(employees):
    for employee in employees:
        print(f'{employee.id_number} - {employee.name}')


def show_employees(employees_array, employee_type):
    employees_array = [x for x in employees_array if x.type == employee_type]
    for employee in employees_array:
        print(f'{employee.id_number} - {employee.name}')


def show_employee_details(employee):
    print("______________________________________")
    print(f'Nome: {employee.name}')
    print(f'Tipo: {employee.type}')
    print(f'Endereco: {employee.address}')
    print("______________________________________")


def get_employee_by_id(employees, employee_id):
    return [x for x in employees if x.id_number == employee_id]


if __name__ == '__main__':
    print('Welcome to the payroll System program')
    running = True
    employees = []

    open_seed_file()

    while running:
        show_menu()
        options = int(input("Selecione a opcão que deseja acessar: "))

        if options == 1:
            add_employee()
        elif options == 2:
            if len(employees) != 0:
                show_all_employees(employees)
            else:
                print("Não há funcionários cadastrados")
        elif options == 3:
            delete_employee(len(employees))
        elif options == 4:
            print("Selecione o funcionário que deseja adicionar o Cartão de Ponto:\n")
            show_employees(employees, "Horista")
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            add_timecard(selected_employee)
        elif options == 5:
            print("Selecione o funcionário que deseja adicionar o Resultado de Venda:\n")
            show_employees(employees, "Comissionado")
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            add_sale(selected_employee)
        elif options == 6:
            running = False
            print("Exiting\n")
