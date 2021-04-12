from Models.PaymentMethod import PaymentMethod


class MailCheck(PaymentMethod):

    def __init__(self, value, id, type, address):
        super().__init__(value, id, type)
        self._address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address
