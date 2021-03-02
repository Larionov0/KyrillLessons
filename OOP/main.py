class Human:
    name = 'Human'
    is_male = True
    age = 0
    money = 0

    def say_hi(self):
        print(f'{self.name}: Hello')

    def say_hi_to_someone(self, other_human):
        print(f'{self.name}: Hello, {other_human.name}')

    def grow_up(self):
        self.age += 1
        word = 'ему' if self.is_male else 'ей'
        print(f'{self.name} подрос на год! Теперь {word} {self.age} лет')
        if self.age == 18:
            print(f'Теперь {self.name} совершеннолетний!')
        elif self.age == 60:
            print(f'Теперь {self.name} пенсионер!')

    def __call__(self, job):  # as functions
        print(f'Наш {self.name} на работе: {job}')


h1 = Human()
h1.name = 'Bob'
h1.age = 16
h1.money = 1000

h2 = Human()
h2.name = 'Alice'
h2.is_male = False
h2.age = 21
h2.money = 10000

h1('повар')

