""" dictionnaire = {"utilisateur": "Paul"}
dictionnaire["utilisateur"] = "Julie"

print(dictionnaire)  """

""" employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]


print(employes)
print(age_paul) """


from pathlib import Path

p = Path("C:/Users/Pavel/Desktop/formation_python/projet_trieur/data")
print(p.name)
print(p.parent)
print(p.stem)
print(p.suffix)
print(p.suffixes)
print(p.parts)
print(p.exists())
print(p.is_dir())
print(p.is_file())
