class PaymentMethod:

    def __init__(self, value, id, type):
        self._value = value
        self._id = id
        self._type = type

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def id(self):
        return self._id
