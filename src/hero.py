class Hero:
    def __init__(self, name, health, attack, walk_speed, attack_speed, *items):
        self.name = name
        self.health = health
        self.attack = attack
        self.items = items
        self.walk_speed = walk_speed
        self.attack_speed = attack_speed

    def __len__(self):
        print(f"У героя в инвентаре {len(self.items)} предметов")
        if len(self.items) > 0:
            print(self.items)

    def speed(self):
        print(
            f"Ваша скорость передвижения равна {self.walk_speed}\nСкорость атаки равна {self.attack_speed}"
        )


class Warrior(Hero):
    def __init__(self, name, health, attack, walk_speed=50, attack_speed=15, *items):
        super().__init__(name, health, attack, walk_speed, attack_speed, *items)

    def __str__(self):
        return f"Воин {self.name} имеет {self.health} HP и наносит {self.attack} DMG"

    def speed(self):
        super().speed()

    @staticmethod
    def weapon():
        print("Ваше оружие - это большой двуручный меч!")


class Dodger(Hero):
    def __init__(self, name, health, attack, walk_speed=90, attack_speed=30, *items):
        super().__init__(name, health, attack, walk_speed, attack_speed, *items)

    def __str__(self):
        return f"Ловкач {self.name} имеет {self.health} HP и наносит {self.attack} DMG"

    def speed(self):
        super().speed()

    @staticmethod
    def weapon():
        print("Ваше оружие - это два небольших кинжала!")


class Archer(Hero):
    def __init__(self, name, health, attack, walk_speed=70, attack_speed=25, *items):
        super().__init__(name, health, attack, walk_speed, attack_speed, *items)

    def __str__(self):
        return f"Лучник {self.name} имеет {self.health} HP и наносит {self.attack} DMG"

    def speed(self):
        super().speed()

    @staticmethod
    def weapon():
        print("Ваше оружие - это лук со стрелами!")


class Wizard(Hero):
    def __init__(self, name, health, attack, walk_speed=80, attack_speed=10, *items):
        super().__init__(name, health, attack, walk_speed, attack_speed, *items)

    def __str__(self):
        return f"Маг {self.name} имеет {self.health} HP и наносит {self.attack} DMG"

    def speed(self):
        super().speed()

    @staticmethod
    def weapon():
        print("Ваше оружие - это волшебная палочка!")


class Tramp(Hero):
    def __init__(self, name, health, attack, walk_speed=100, attack_speed=50, *items):
        super().__init__(name, health, attack, walk_speed, attack_speed, *items)

    def __str__(self):
        return f"Бродяга {self.name} имеет {self.health} HP и наносит {self.attack} DMG"

    def speed(self):
        super().speed()

    @staticmethod
    def weapon():
        print("Ваше оружие - это кулаки!")


class Enemy:
    def __init__(self, name, health, attack, attack_speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed

    def __str__(self):
        return f"Характеристики врага:\nHP: {self.health}\nDMG: {self.attack}\nСкорость атаки: {self.attack_speed}"


class Goblin(Enemy):
    def __init__(self, name="Гоблин", health=10, attack=10, attack_speed=50):
        super().__init__(name, health, attack, attack_speed)

    def __str__(self):
        super().__str__()


class Ork(Enemy):
    def __init__(self, name="Орк", health=20, attack=20, attack_speed=30):
        super().__init__(name, health, attack, attack_speed)

    def __str__(self):
        super().__str__()


class Golem(Enemy):
    def __init__(self, name="Голем", health=30, attack=30, attack_speed=10):
        super().__init__(name, health, attack, attack_speed)

    def __str__(self):
        super().__str__()