"""
import java.util.Scanner;


public class Employee {
    private String name;
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


    private String address;
    private int salary;
    private String type;
    private Scanner input = new Scanner(System.in);
    private String answer;

    public Employee(){
        System.out.println("Insira o nome do funcionário: ");
        answer = input.nextLine();
        this.name = answer;
        System.out.println("Insira o endereço do funcionário: ");
        answer = input.nextLine();
        this.address = answer;
        System.out.println("Insira o tipo de funcionário: ");
        answer = input.nextLine();
        this.type = answer;
    }
}

"""
