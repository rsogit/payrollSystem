# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Models.Hourly import Hourly
from Models.Salaried import Salaried
from Models.Commissioned import Commissioned

id_counting: int = 1


def show_menu():
    print("=======Sistema de Folha de Pagamento========\n")
    print("MENU PRINCIPAL\n")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Deletar Funcionário")
    print("4 - Sair\n")


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


def show_all_employees():
    for employee in employees:
        print(f'{employee.id_number} - {employee.name}')


def show_employee_details(employee):
    print("______________________________________")
    print(f'Nome: {employee.name}')
    print(f'Tipo: {employee.type}')
    print(f'Endereco: {employee.address}')
    print("______________________________________")


if __name__ == '__main__':
    print('Welcome to the payroll System program')
    running = True
    employees = []
    while running:
        show_menu()
        options = int(input("Selecione a opcão que deseja acessar: "))

        if options == 1:
            add_employee()
        elif options == 2:
            if len(employees) != 0:
                show_all_employees()
            else:
                print("Não há funcionários cadastrados")
        elif options == 3:
            if len(employees) != 0:
                print("Digite o número do funcionário que deseja deletar: ")
                show_all_employees()
                employee_number = int(input("\n"))
                for index, employee in enumerate(employees):
                    if employee.id_number == employee_number:
                        deleted_employee = employees.pop(index)
                        print(f'Funcionário "{deleted_employee.name}" deletado com sucesso!')
        elif options == 4:
            running = False
            print("Exiting\n")
