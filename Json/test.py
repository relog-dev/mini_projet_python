import json

with open("Json/data.json", "r") as f:
    donnees = json.load(f)

donnees.append(int(input("nique ta mère")))

with open("Json/data.json", "w") as f:
    json.dump(donnees, f, indent=4)