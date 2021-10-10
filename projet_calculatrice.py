nombre_1 = input("Entrez un premier nombre: ")
nombre_2 = input("Entrez un deuxieme nombre: ")

if nombre_1.isdigit() and nombre_2:
    print (f"Le résultat de l'addition de {nombre_1} avec {nombre_2} est égal à {int(nombre_1) + int(nombre_2)}")
else:
    print ("Veuillez entrer deux nombres valides")