class Account:
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    #@amount.setter
    #def amount(self, amount):
    #    self.__amount = amount

    def transfer(self, other, to_tr):
        if self.__amount - to_tr >= 0:
            self.__amount -= to_tr
            other.__amount += to_tr


nick = Account(50)
mike = Account(150)
print(nick.get_amount(), mike.get_amount())

nick.set_amount(nick.get_amount() - 50)
mike.set_amount(mike.get_amount() + 500)
print(nick.get_amount(), mike.get_amount())
