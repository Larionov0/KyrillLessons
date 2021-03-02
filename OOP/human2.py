import datetime


class Human:
    def __init__(self, name, is_male, date_of_birth, money):
        self._name = name
        self._is_male = is_male
        self._date_of_birth = datetime.date(year=date_of_birth[2], month=date_of_birth[1], day=date_of_birth[0])
        self._money = money

    @property
    def age(self):
        now = datetime.datetime.now().date()
        t_delta = now - self._date_of_birth
        return round(t_delta.days / 365, 2)

    def say_hi(self):
        print(f'{self._name}: Hello')

    def say_hi_to_someone(self, other_human):
        print(f'{self._name}: Hello, {other_human.name}')


h1 = Human('Bob', True, [12, 2, 2000], 1000)
h2 = Human('Alice', False, [9, 12, 1998], 12450)

print(h1.age)
print(h2.age)
