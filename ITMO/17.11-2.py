def fun(a: int, b: int) -> int:
    return a * b


class Account:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount


a: int = 5
print(a)
print(fun(4.5, 5.4))
mike = Account(150.5)
