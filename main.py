# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def show_menu():
    print("=======Sistema de Folha de Pagamento========\n")
    print("MENU PRINCIPAL\n")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Sair\n")


if __name__ == '__main__':
    print_hi('Welcome to the payroll System program')
    running = True
    while running:
        show_menu()
        options = int(input("Selecione a opcão que deseja acessar: "))

        if options == 1:
            print("First Option\n")
        elif options == 2:
            print("Second Option\n")
        elif options == 3:
            running = False
            print("Exiting\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




"""
public class Main {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int options;
        boolean running = true;
        ArrayList<Employee> allEmployees = new ArrayList<Employee>();

        while(running)
        {
            showMenu();
            options = input.nextInt();
            input.nextLine();

            if(options == 1)
            {
                Employee employee = new Employee();
                allEmployees.add(employee);
                System.out.println("Adicione um salário para o funcionário");
                options = input.nextInt();
                employee.setSalary(options);
                if(employee!=null)System.out.println("Funcionário cadastrado com sucesso!");
                else System.out.println("Erro no cadastro do funcionário!");
            } else if(options == 2) {
                if(allEmployees.size() == 0) System.out.println("Não há funcionários cadastrados");
                showEmployees(allEmployees);
            }
            else if(options == 3){
                running = false;
            }
        }

    }

    public static void showMenu() {
        System.out.println("=======Sistema de Folha de Pagamento========");
        System.out.println("");
        System.out.println("MENU PRINCIPAL");
        System.out.println();
        System.out.println("1 - Cadastrar Funcionário");
        System.out.println("2 - Listar Funcionários");
        System.out.println("3 - Sair");
    }

    private static void showEmployees(ArrayList<Employee> allEmployees) {
        for(Employee count: allEmployees){
            System.out.println("");
            System.out.println("- Nome: " + count.getName());
            System.out.println("-------- Endereço: " + count.getAddress());
            System.out.println("-------- Tipo: " + count.getType());
            System.out.println("-------- Salário: " + count.getSalary());
            System.out.println("--------------------------------");
            System.out.println("");
        }
    }
}
"""