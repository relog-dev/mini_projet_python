mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0:
    print (mdp_trop_court.upper())

elif len(mdp) < 8:
    print (mdp_trop_court.capitalize())

elif mdp.isalpha()==True:
    print ("votre mot de passe ne contient que des lettes".capitalize())

elif mdp.isdigit()==True:
    print ("votre mot de passe ne contient que des nombres".capitalize())

elif mdp.isalnum()==True:
    print("inscription terminée".capitalize())
else: 
    print("votre mot de passe ne doit pas contenir de caractère spéciaux".capitalize())