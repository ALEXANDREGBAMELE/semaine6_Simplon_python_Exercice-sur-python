#Exercice 3
with open("file.txt", "r") as fichier:
    contenu = fichier.read().replace("\n", " ")

print(contenu)

