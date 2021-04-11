from Models.PaymentMethod import PaymentMethod


class Deposit(PaymentMethod):

    def __init__(self, value, id, type, agency, account):
        super().__init__(value, id, type)
        self._agency = agency
        self._account = account
