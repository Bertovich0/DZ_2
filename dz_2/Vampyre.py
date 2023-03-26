from leson_2.personah import Character
from colorama import Fore, Style

class Vampyre(Character):
    def __init__(self, name='', health=100, damage=1, defence=0, color=Fore.LIGHTWHITE_EX):
        super().__init__(name, health, damage, defence, color)

    def attack(self, target):
        damage_dealt = self.damage
        target.take_damage(damage_dealt)
        self.heal(int(damage_dealt * 0.1))

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def get_stats(self):
        return \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Здоровье: {self.health}\n' \
            f'Урон: {self.damage}\n' \
            f'Защита {self.defence}\n' \
            f'Тип: Вампир\n' \
            f'{Style.RESET_ALL}'
