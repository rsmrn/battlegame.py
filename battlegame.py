"""
Declaring variables and hitpoints and damage

"""

wizard = "Wizard"
elf = "Elf"
human ="Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

"""
Prompt the player to choose from a list of options
"""
character = input("1.Wizard\n 2.Elf \n 3.Human \n Choose your character ")

"""
Set up infinite while loop to handle player choice
"""
while True:
    if character =="1" :
        character = "wizard"
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character =="2" :
        character = "elf"
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character =="3" :
        character = "human"
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
print("You have chosen the character: " + character)
print("Health: " + str(my_hp))
print("Damage: " + str(my_damage))    

"""
Battle with the Dragon
"""
while True:
    """Players turn"""
    dragon_hp = dragon_hp - my_damage
    print("The", character,"damaged the Dragon!")
    print("Dragon's remaining HP:",dragon_hp)
    if dragon_hp <=0:
        print("The dragon has lost the battle")
        break
    """Dragon's turn"""
    my_hp = my_hp - dragon_damage
    print("The dragon strikes back at the",character)
    print(character,"remaining HP:",my_hp)
    if my_hp <=0:
        print("The",character,"has lost the battle")
        break

   
