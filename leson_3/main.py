from leson_2.personah import Character
from berserk import Berserk
from  colorama import Fore , Style

player1 = Berserk(name='Ignat', health=70, damage=2,
                  color=Fore.LIGHTBLUE_EX)
print(player1)

player2 = Character(name="Ilia", health=90, damage=1,
                    color=Fore.LIGHTRED_EX)
print(player2)

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)