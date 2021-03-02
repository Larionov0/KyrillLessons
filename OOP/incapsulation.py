import random


class Hero:
    def __init__(self, name, hp, attack, armor, magic):
        self._name = name
        self.__set_hp(hp)
        self._attack = attack
        self._armor = armor
        self._magic = magic
        self._is_alive = True

    @property
    def name(self):
        return self._name

    @property
    def magic(self):  # getter
        return self._magic

    @magic.setter
    def magic(self, value):  # setter
        if value > 10 or value < 0:
            raise Exception('Магия должна быть ограничена от 0 до 10')
        self._magic = value
        print(f"Магия для {self.name} изменилась. Теперь = {self._magic}")

    def say_hi(self):
        print(f"{self._name}: Hello")

    def __set_hp(self, hp):
        self.hp = self.max_hp = hp

    def get_damage(self, damage):
        remaining_damage = damage - self._armor
        print(f'В {self._name} прошло {remaining_damage} / {damage} урона.')
        if remaining_damage > 0:
            self.loose_hp(remaining_damage)

    def loose_hp(self, damage):
        self.hp -= damage
        print(f"{self._name} потерял {damage} здоровья. Осталось {self.hp} / {self.max_hp} hp.")
        if self.hp <= 0:
            self.__die()

    def __die(self):
        self.is_alive = False
        print(f'{self._name} откинулся.')

    def normal_attack(self, enemy):
        print(f'{self._name} совершает удар по {enemy.name}!')
        enemy.get_damage(self._attack)


class Assassin(Hero):
    def __init__(self, name, hp, attack, armor, magic, crit_koef=2):
        super().__init__(name, hp, attack, armor, magic)
        self.crit_koef = crit_koef

    def normal_attack(self, enemy):
        print(f'{self._name} совершает удар по {enemy.__name}!')
        damage = self._attack
        if random.randint(1, 100) <= 30:
            print('*crit*')
            damage *= self.crit_koef
        enemy.get_damage(damage)


class Archer(Hero):
    def __init__(self, name, hp, attack, armor, magic, avoid_chance=25):
        """
        :param avoid_chance: int,  %
        """
        super().__init__(name, hp, attack, armor, magic)
        self.avoid_chance = avoid_chance

    def get_damage(self, damage):
        if random.randint(1, 100) <= self.avoid_chance:
            print(f"{self._name} увернулся!")
            return

        super().get_damage(damage)

    def test(self):
        print(self._name)


def poisoning(hero, damage):
    hero.hp -= damage
    hero.name = 'Goga'


h1 = Archer('Tommy', 22, 5, 1, 0)
h2 = Hero('Puzan', 40, 2, 2, 0)
h3 = Assassin('Hunter', 25, 4, 2, 0, 2)

h1.magic = 4
print(h1.magic)
