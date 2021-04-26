import json
import datetime
from datetime import datetime
from Models.TimeCard import TimeCard
from Models.Sale import Sale
from Models.Hourly import Hourly
from Models.Salaried import Salaried
from Models.Commissioned import Commissioned

id_counting: int = 1
payment_schedules = ["weekly 1 friday", "weekly 2 friday", "monthly $"]


def show_menu():
    print("=======Sistema de Folha de Pagamento========\n")
    print("MENU PRINCIPAL\n")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Editar Funcionário")
    print("4 - Remover Funcionário")
    print("5 - Adicionar cartão de ponto para um funcionário")
    print("6 - Adicionar Resultado de Venda para um funcionário")
    print("7 - Adicionar Taxa de Servico Sindical para um funcionário")

    print("8 - Sair\n")


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


def edit_employee(size, employee_number):
    if employee_number <= size:
        employee = employees[employee_number-1]
        print(f'Digite a opcão que deseja editar do funcionário: {employee.name}')
        print("1 - Nome")
        print("2 - Tipo")
        print("3 - Endereco")
        print("4 - Método de pagamento")
        print("5 - Participacão no sindicato")
        if employee.union_info.is_active:
            print("6 - ID no sindicato")
            print("7 - Taxa sindical fixa")
        try:
            answer = int(input())
        except:
            print("Digite um número válido.")

        if answer == 1:
            new_name = input(f'Digite o novo nome do funcionário "{employee.name}":\n')
            employee.name = new_name
            print("Nome alterado com sucesso")
        elif answer == 2:
            new_type = int(input(f'Selecione o novo tipo do funcionário "{employee.name}":\n'
                             f'1 - Horista\n'
                             f'2 - Comissionado\n'
                             f'3 - Assalariado\n'))
            if new_type == 1:
                employee = Hourly(employee.name,
                                  employee.address,
                                  employee.id_number)
                print(f'O funcionário {employee.name} agora é do tipo {employee.type}\n')
            elif new_type == 2:
                employee = Commissioned(employee.name,
                                        employee.address,
                                        employee.id_number)
                print(f'O funcionário {employee.name} agora é do tipo {employee.type}\n')
            elif new_type == 3:
                employee = Salaried(employee.name,
                                    employee.address,
                                    employee.id_number)
                print(f'O funcionário {employee.name} agora é do tipo {employee.type}\n')
            else:
                print("o funcionário não foi editado, tente novamente.")
                return
        elif answer == 3:
            new_address = input(f'Digite o novo endereco do funcionário: {employee.name}')
            employee.address = new_address
            print("Endereco alterado com sucesso")
        elif answer == 4:
            print("implement edit paymentMethod")
        elif answer == 5:
            if employee.union_info.is_active:
                opt = int(input(f'Atualmente o funcionário {employee.name} está ativo no sindicato, '
                            f'deseja deixá-lo inativo?\n'
                      f'1 - Sim\n'
                      f'2 - Não\n'))
            else:
                opt = int(input(f'Atualmente o funcionário {employee.name} está inativo no sindicato, '
                            f'deseja deixá-lo ativo?\n'
                      f'1 - Sim\n'
                      f''f'2 - Não\n'))
            if opt == 1:
                employee.union_info.is_active = True
            elif opt == 2:
                employee.union_info.is_active = False
                if not (employee.union_info.monthly_tax > 0):
                    new_taxes = float(input("Adicione a taxa mensal fixa do sindicato para esse funcionário: R$ "))
                    employee.union_info.monthly_tax = new_taxes
            else:
                print("Entrada inválida, tente novamente.")
        elif answer == 6:
            print("implement edit syndical ID feature")
        elif answer == 7:
            new_taxes = float(input("Adicione a nova taxa mensal fixa do sindicato para esse funcionário: R$ "))
            employee.union_info.monthly_tax = new_taxes
        elif answer == 8:
            print("Voltando para o menu principal...")
        elif answer > 8:
            print("Por favor, selecione um número válido")
        else:
            print("Retornando ao menu principal...")


def delete_employee(size, employee_number):
    if size != 0:
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


def show_union_employees(employees_array):
    for employee in employees_array:
        print(f'{employee.id_number} - {employee.name}')


def get_union_employees(employees_array):
    employees_array = [x for x in employees_array if x.union_info.is_active]
    return employees_array


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
                print("Selecione")
            else:
                print("Não há funcionários cadastrados")
        elif options == 3:
            print("Digite o ID do funcionário que deseja editar: ")
            show_all_employees(employees)
            employee_number = int(input("\n"))
            edit_employee(len(employees), employee_number)
        elif options == 4:
            print("Digite o ID do funcionário que deseja deletar: ")
            show_all_employees(employees)
            employee_number = int(input("\n"))
            delete_employee(len(employees), employee_number)
        elif options == 5:
            print("Digite o ID do funcionário que deseja adicionar o Cartão de Ponto:\n")
            show_employees(employees, "Horista")
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            add_timecard(selected_employee)
        elif options == 6:
            print("Digite o ID do funcionário que deseja adicionar o Resultado de Venda:\n")
            show_employees(employees, "Comissionado")
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            add_sale(selected_employee)
        elif options == 7:
            print("Digite o ID do funcionário que deseja adicionar a Taxa de Servico Sindical:\n")
            union_employees = get_union_employees(employees)
            if len(union_employees) > 0:
                show_union_employees(union_employees)
                option = int(input(""))
                selected_employee = get_employee_by_id(employees, option).pop()
                selected_employee.union_info.add_service_fee()
            else:
                print("Não há funcionários ativos no sindicato")
        elif options == 8:
            print("Rodando folha de pagamento para hoje")

        elif options == 9:
            running = False
            print("Exiting\n")
