class Employee:
    _type: str

    def __init__(self, name, address, id_number):
        self._name = name
        self._address = address
        self._id_number = id_number

    @property
    def type(self):
        return self._type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def id_number(self):
        return self._id_number
