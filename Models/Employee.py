from Models.UnionMember import UnionMember
from pandas.tseries.offsets import BMonthEnd
import pandas as pd
from datetime import datetime
from datetime import date


def get_last_business_day():
    d = datetime.now()
    offset = BMonthEnd()
    return offset.rollforward(d)


def get_week_day(week_day):
    if week_day == "monday" or week_day == "segunda":
        day = "MON"
    elif week_day == "tuesday" or week_day == "terca" or week_day == "terça":
        day = "TUE"
    elif week_day == "wednesday" or week_day == "quarta":
        day = "WED"
    elif week_day == "thursday" or week_day == "quinta":
        day = "THU"
    elif week_day == "friday" or week_day == "sexta":
        day = "FRI"
    elif week_day == "saturday" or week_day == "sabado" or week_day == "sábado":
        day = "SAT"
    elif week_day == "sunday" or week_day == "domingo":
        day = "SUN"

    return day


class Employee:
    _type: str
    _union_info: UnionMember
    _last_pay_date: date
    _schedule_type: str
    _schedule: [date] = []

    def __init__(self, name, address, id_number, schedule_type):
        self._name = name
        self._address = address
        self._id_number = id_number
        self._schedule_type = schedule_type
        self._last_pay_date = datetime.now().date()
        self._union_info = UnionMember()
        self._schedule = self.set_schedule(schedule_type)

    def set_schedule(self, schedule_type: str):
        schedule_types = schedule_type.split(" ")
        hour = self._last_pay_date
        first_frequency = schedule_types[0]
        try:
            day_frequency = int(schedule_types[1])
        except:
            day_frequency = schedule_types[1]
        if len(schedule_types) < 3:
            weekday_frequency = "monday"
        else:
            weekday_frequency = schedule_types[2]

        # Caso a frequência seja mensal, gera o intervalo com o offset do dia n.
        # Caso o dia seja "$", gera o intervalo com o offset para o último dia útil
        if first_frequency == "monthly" or first_frequency == "mensal":
            if isinstance(day_frequency, int):
                if 0 < day_frequency <= 31:
                    range = pd.date_range(hour, periods=12, freq='MS') \
                            + pd.DateOffset(days=(day_frequency-1))
                    return range
                else:
                    print("Selecione um dia do mês válido")
            elif day_frequency == "$":
                self._schedule.append(get_last_business_day())
            else:
                print("A expressão de agenda de pagamento customizado está inválida, "
                      "tente novamente no formato 'weekly 2 friday', por exemplo")

        # Caso a frequência seja semanal, gera o intervalo com o offset no dia da semana.
        elif first_frequency == "weekly" or first_frequency == "semanal":
            if weekday_frequency:
                if isinstance(day_frequency, int):
                    range = pd.date_range(hour, periods=12, freq=f'{day_frequency}W-{get_week_day(weekday_frequency)}')
                    return range
            else:
                print("A expressão de agenda de pagamento customizado está inválida, "
                      "tente novamente no formato 'weekly 2 friday', por exemplo")
        else:
            return []

    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        self._schedule_type = schedule_type

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule_type(self, schedule):
        self._schedule = schedule

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
