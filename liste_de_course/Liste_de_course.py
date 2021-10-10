import sys
import json

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]



while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Veuillez choisir une option valide...")
        continue

    if user_choice == "1":  # Ajouter un élément
        with open("liste_de_course/data_liste.json", "r") as f:
            item = json.load(f)
        
        item.append(input("Entrez le nom d'un élément à ajouter à la liste de courses : "))
        
        with open("liste_de_course/data_liste.json", "w") as f:
            json.dump(item, f, indent=4)
        
        print(f"L'élément {item} a bien été ajouté à la liste.")
        
    elif user_choice == "2":  # Retirer un élément
        with open("liste_de_course/data_liste.json", "r") as f:
            item = json.load(f)
        
        item.remove(input("Entrez le nom d'un élément à retiré de la liste de courses : "))
        
        with open("liste_de_course/data_liste.json", "w") as f:
            json.dump(item, f, indent=4)

    elif user_choice == "3":  # Afficher la liste
        with open("liste_de_course/data_liste.json", "r") as f:
            item = json.load(f)
        print(f"Vous avez : {item} dans votre liste de course")

    elif user_choice == "4":  # Vider la liste
        with open("liste_de_course/data_liste.json", "r") as f:
            item = json.load(f)

        item.clear()
        
        with open("liste_de_course/data_liste.json", "w") as f:
            json.dump(item, f, indent=4)
        print("Tout les éléments de la liste on été supprimer.")

    elif user_choice == "5":  # Quitter
        print("À bientôt !")
        sys.exit()

    print("-" * 50)