from Models.PaymentMethod import PaymentMethod


class InHandsCheck(PaymentMethod):

    def __init__(self, value, id, type):
        super().__init__(value, id, type)