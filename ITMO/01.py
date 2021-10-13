class Person:

    def __init__(self, arms_count, name):
        self.name = name
        self.arms_count = arms_count

    def greet(self):
        print(f'Hi {self.name}! \nWoah, you have {self.arms_count} arms? Cool!')

    # "magic" attributes

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f'Person<name={self.name}>'


if __name__ == "__main__":
    me = Person(734, "Joseph")
    clone = Person(734, "Joseph")
    you = Person(5, "Bernard")

    me.greet()
    you.greet()

    print(len(dir(str)))

    print(me == clone)
