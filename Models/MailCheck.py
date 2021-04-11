from Models.PaymentMethod import PaymentMethod


class MailCheck(PaymentMethod):

    def __init__(self, value, id, type, address):
        super().__init__(value, id, type)
        self._address = address
