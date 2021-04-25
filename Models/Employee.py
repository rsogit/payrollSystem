from Models.UnionMember import UnionMember


class Employee:
    _type: str
    _union_info: UnionMember

    def __init__(self, name, address, id_number):
        self._name = name
        self._address = address
        self._id_number = id_number
        self._union_info = UnionMember()

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

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

    @property
    def union_info(self):
        return self._union_info
