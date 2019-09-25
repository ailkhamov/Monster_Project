from moster_class import *

monster1 = monster("Medusa",2,"Heavy","Strong Punch",True)
monster2 = monster("Empusa",4, "Beaver","Kong-Fu", False)
monster3 = monster("Cerberus",2, "Fox", "Boxing", True)

print("Welcome to the monster game!")
print("Choose three of the following monster")
print("monster 1: Medusa")
print("monster 2: Empusa")
print("monster 3: Cerberus")

choose_monster = input("Choose your monster").lower().capitalize()

while True:


    if choose_monster == "Medusa":
        print(f' You have chosen {monster1.name}. You have {monster1.eye} eyes. Your fur jacket is {monster1.fur}. Your skill is {monster1.skiil}')
        break

    elif choose_monster == "Empusa":
       print(f' You have chosen {monster2.name}. You have {monster2.eye} eyes. Your fur jacket is {monster2.fur}. Your skill is {monster2.skiil}')
       break
    elif choose_monster == "Cerberus":
        print(f' You have chosen {monster3.name}. You have {monster3.eye} eyes. Your fur jacket is {monster3.fur}. Your skill is {monster3.skiil}')
        break
    else:
        print("The monster you have entered is incorrect")
        if True:
            choose_monster  = input("Choose your monster again")

choice_scare = input("You see your ennemy ahead of you. Would you like to scare him ?").lower()
monster1.scare(choice_scare)

eat = input("You lost some health scaring the monster away! Do you want to eat?").lower
monster1.eat(eat)
print("---------------------------------------------------------------------")
print("You can choose to transform your monster.")
print("Choose three of the following transformation")
print(" 1: Dragons")
print(" 2: Unicorns")
print(" 3: Giant Human")
transfrom = input()
monster1.transfrom(transfrom)