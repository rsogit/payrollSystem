class ServiceTaxes:
    _value: float
    _date: str

    def __init__(self, value=None, date=None):
        if value and date:
            self._value = value
            self._date = date
        else:
            self._value = input("Digite o valor da nova taxa de servico: R$")
            self._date = input("Digite a data da nova taxa de servico no formato (DD/MM/AAAA): ")
