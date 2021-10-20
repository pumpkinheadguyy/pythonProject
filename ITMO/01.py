class Person:

    def __init__(self, arms_count, name):
        self.name = name
        self.arms_count = arms_count

    def greet(self):
        print(f'Hi {self.name}! \nWoah, you have {self.arms_count} arms? Cool!')


if __name__ == "__main__":
    me = Person(734, "Joseph")
    you = Person(5, "Bernard")

    me.greet()
    you.greet()
    print(dir(str))
