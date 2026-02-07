from random import randint

from hero import *


def is_valid_digit(value):
    if value.isdigit():
        return int(value)
    value = input("Введите число!!!\n")
    return is_valid_digit(value)


def battle(character, enemy):
    print(f"Начинается бой между {character.name} и {enemy.name}!!!")
    while character.health > 0 and enemy.health > 0:
        if enemy.attack_speed <= character.attack_speed:
            enemy.health -= character.attack
            print(
                f"Вы наносите удар {character.attack} DMG!\n{enemy.name} остался с {enemy.health} HP"
            )
            input()
            if character.health <= 0 or enemy.health <= 0:
                break
            character.health -= enemy.attack
            print(
                f"{enemy.name} наносит удар {enemy.attack} DMG!\nУ вас остается {character.health} HP"
            )
            input()
        else:
            character.health -= enemy.attack
            print(
                f"{enemy.name} наносит удар {enemy.attack} DMG!\nУ вас остается {character.health} HP"
            )
            input()
            if character.health <= 0 or enemy.health <= 0:
                break
            enemy.health -= character.attack
            print(
                f"Вы наносите удар {character.attack} DMG!\n{enemy.name} остался с {enemy.health} HP"
            )
            input()
    if character.health > 0:
        print("Поздравляю вы победили!!!")
        print(f"Но у вас осталось {character.health} HP")
        return True
    else:
        print(
            "Вы проиграли в этой схватке!\nНичего страшного!\nВ следующий раз вы обязательно победите!!!"
        )
        input()
        return False


def random_enemy(b):
    enemy_type = randint(1, b)
    if enemy_type == 1:
        return Goblin()
    elif enemy_type == 2:
        return Ork()
    else:
        return Golem()


print("Добро пожаловать в игру!!!")
print("Кем вы хотите быть?\n1. Воином\n2. Ловкачом\n3. Лучником\n4. Магом")
type_hero = input("Введите цифру:")
type_hero = is_valid_digit(type_hero)
name = input("Как вы назовете своего героя?\n")
print()
if type_hero == 1:
    print("Итак, вы решили стать воином!")
    health = randint(120, 140)
    attack = randint(30, 35)
    hero = Warrior(name, health, attack)
elif type_hero == 2:
    print("Итак, вы решили стать ловкачом!")
    health = randint(80, 100)
    attack = randint(20, 25)
    hero = Dodger(name, health, attack)
elif type_hero == 3:
    print("Итак, вы решили стать лучником!")
    health = randint(70, 90)
    attack = randint(25, 30)
    hero = Archer(name, health, attack)
elif type_hero == 4:
    print("Итак, вы решили стать магом!")
    health = randint(60, 80)
    attack = randint(35, 40)
    hero = Wizard(name, health, attack)
else:
    print("Вы решили стать никем, иначе говоря бродягой!")
    health = randint(20, 40)
    attack = randint(5, 10)
    hero = Tramp(name, health, attack)

print("У вас следующие характеристики:")
print(hero.__str__())
hero.speed()
input()
while True:
    opponent = random_enemy(3)
    print(
        f"Вам на пути попался {opponent.name}!!!\nВы должны сразиться с ним! В атаку!!!"
    )
    input()
    if battle(hero, opponent):
        chs = input("Хотите продолжить путь? (Введите Y, если да):")
        print()
        if chs.lower() != "y":
            break
    else:
        break
print(
    "Игра закончена!\nБыло очень весело, надеюсь ты вернешься путник!\nУдачи тебе в дальнейших странствиях!"
)
input()