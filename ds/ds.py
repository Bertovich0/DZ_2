import random


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, other):
        damage = random.randint(1, self.damage)
        other.health -= damage
        print(f"{self.name} нанес {other.name} {damage} единиц урона.")

    def is_alive(self):
        return self.health > 0


def main():
    player1 = Character("Игрок 1", 50, 10)
    player2 = Character("Игрок 2", 50, 10)

    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if not player2.is_alive():
            print(f"{player2.name} проиграл.")
            break
        player2.attack(player1)
        if not player1.is_alive():
            print(f"{player1.name} проиграл.")
            break


if __name__ == "__main__":
    main()
