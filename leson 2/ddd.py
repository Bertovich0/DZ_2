from  personah import  Character
from  colorama import Fore

player1 = Character(name='gaijin', health=100, damage=150,
                    color=Fore.LIGHTRED_EX)
print(player1)

player2 = Character(name='credit card', health=150, damage=1,
                    color=Fore.LIGHTBLUE_EX)
print(player2)

player1.attack(player2)


print(player1)
print(player2)

