class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет №{self.__num}, принадлежащий {self.__surname}, был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет №{self.__num}, принадлежащий {self.__surname}, был закрыт.")

    @classmethod
    def set_usd_rate(cls, new_rate):
        cls.rate_usd = new_rate

    @classmethod
    def set_eur_rate(cls, new_rate):
        cls.rate_eur = new_rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_num(self):
        return self.__num

    def set_num(self, num):
        self.__num = num

    def get_percent(self):
        return self.__percent

    def set_percent(self, percent):
        self.__percent = percent

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def print_balance(self):
        print(f'Текущий баланс: {self.__value} {Account.suffix}')

    def print_info(self):
        print('Информация о счете:')
        print('-' * 20)
        print(f'№{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению, у Вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.set_surname("Дюма")
acc.set_num('54321')
acc.set_percent(0.15)
acc.print_info()
acc.add_percents()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
print()
