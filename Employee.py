class Employee:
    salary: int
    name: str
    address: str
    kind: str

    def __init__(self):
        self.name = input("Insira o nome do funcionário: ")
        self.address = input("Insira o endereço do funcionário: ")
        self.kind = input("Insira o tipo do funcionário: ")
