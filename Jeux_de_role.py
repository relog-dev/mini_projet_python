from random import randint

Attaque_ennemi = randint(5, 15)
Mon_attaque = randint(5, 10)
Mes_PV = 50
PV_ennemi = 50
Nombre_de_potion = 3
Heal = randint(15, 50)

MENU = """Choisissez parmi les 2 options suivantes :
1: 💢 Attaquer
2: 💞 Utiliser une potion
👉 Votre choix : """

MENU_CHOICES = ["1", "2"]

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide")
        continue
    
    if user_choice == "1":
        PV_ennemi -= Mon_attaque
        Mes_PV -= Attaque_ennemi
        print (f"Vous infligez {Mon_attaque} points de dégàt à l'ennemi.")
        print (f"Il reste {PV_ennemi} point de vie à l'ennemi.")
        print (f"L'ennemi viens de vous infligez {Attaque_ennemi} point de dégàt.")
        print (f"Il ne vous reste que {Mes_PV} point de vie.")
    
    elif user_choice == "2":
        if Nombre_de_potion > 0:
            Mes_PV += Heal
            Nombre_de_potion -= 1
            Mes_PV -= Attaque_ennemi
            print (f"Vous prenez une potion, vous venez de récupérez {Heal} point de vie")
            print (f"L'ennemi viens de vous infligez {Attaque_ennemi} point de dégàt.")
            print (f"Il ne vous reste que {Mes_PV} point de vie.")
            print ("Vous venez de passer votre tour.")
            if Nombre_de_potion == 0:
                print ("Vous n'avez plus de potion.")

    

    print("-" * 50)

    if Mes_PV <= 0:
        print("Vous avez perdu !")
        break

    elif PV_ennemi <= 0:
        print("Vous avez Gagné !")
        break

    