from Models.PaymentMethod import PaymentMethod


class Deposit(PaymentMethod):

    def __init__(self, value, id, type, agency, account):
        super().__init__(value, id, type)
        self._agency = agency
        self._account = account

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account
