#Exercice 6 : Modifier l'élément d'une liste imbriquée dans la liste suivante

def modifier_occurrences(liste, ancienne_valeur, nouvelle_valeur):
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            modifier_occurrences(liste[i], ancienne_valeur, nouvelle_valeur)
        elif liste[i] == ancienne_valeur:
            liste[i] = nouvelle_valeur

list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
modifier_occurrences(list1, 58, 5800)
print(list1)
