import random


class Hero:
    def __init__(self, name, hp, attack, armor, magic):
        self.name = name
        self.hp = self.max_hp = hp
        self.attack = attack
        self.armor = armor
        self.magic = magic
        self.is_alive = True

    def say_hi(self):
        print(f"{self.name}: Hello")

    def set_hp(self, hp):
        self.hp = self.max_hp = hp

    def get_damage(self, damage):
        remaining_damage = damage - self.armor
        print(f'В {self.name} прошло {remaining_damage} / {damage} урона.')
        if remaining_damage > 0:
            self.loose_hp(remaining_damage)

    def loose_hp(self, damage):
        self.hp -= damage
        print(f"{self.name} потерял {damage} здоровья. Осталось {self.hp} / {self.max_hp} hp.")
        if self.hp <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        print(f'{self.name} откинулся.')

    def normal_attack(self, enemy):
        print(f'{self.name} совершает удар по {enemy.name}!')
        enemy.get_damage(self.attack)


class Assassin(Hero):
    def __init__(self, name, hp, attack, armor, magic, crit_koef=2):
        super().__init__(name, hp, attack, armor, magic)
        self.crit_koef = crit_koef

    def normal_attack(self, enemy):
        print(f'{self.name} совершает удар по {enemy.name}!')
        damage = self.attack
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
            print(f"{self.name} увернулся!")
            return

        super().get_damage(damage)


def battle(hero1, hero2):
    round = 1
    while hero1.is_alive and hero2.is_alive:
        print(f'--= Раунд {round} =--')
        hero1.normal_attack(hero2)
        print()
        hero2.normal_attack(hero1)
        print()
        round += 1
    print(hero1.hp)
    print(hero2.hp)


h1 = Archer('Tommy', 22, 5, 1, 0)
h2 = Hero('Puzan', 40, 2, 2, 0)
h3 = Assassin('Hunter', 25, 4, 2, 0, 2)


battle(h1, h3)
