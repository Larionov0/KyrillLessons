SLIMES = []


class Slime:
    def __init__(self, name, v, eyes=2):
        self.name = name
        self.v = v
        self.eyes = eyes
        print('Новый слизень создан!!!')
        SLIMES.append(self)  # плохой прием

    def __add__(self, other):  # +
        new_slime = Slime(
            self.name[:len(self.name) // 2] + other.name[len(other.name) // 2:],
            self.v + other.v,
            self.eyes + other.eyes
        )
        return new_slime

    def __str__(self):  # str
        return f"Slime '{self.name}' (v={self.v}; eyes={self.eyes})"

    def __getitem__(self, item):  # []
        """
        ob[3]

        item = 3
        """
        return item ** 2

    def __gt__(self, other):  # >
        return self.v > other.v

    def __repr__(self):
        return "< " + self.__str__() + ' >'


s1 = Slime('Sleezy', 6)

s2 = Slime('Malman', 2, 3)

print(s1 + s2)

