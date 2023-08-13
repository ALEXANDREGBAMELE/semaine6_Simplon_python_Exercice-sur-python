#Exercice 1
# la variable maListe
maListe = [1,2,3,4]
print(maListe)

#inverser la variable maListe
maListe.reverse()
print(maListe)





liste_nombres = [10, 25, 7, 30, 45, 8, 15, 20, 50]

nombres_divisibles_par_5 = [nombre for nombre in liste_nombres if nombre % 5 == 0]

print("Nombres divisibles par 5 :", nombres_divisibles_par_5)

def modifier_occurrences(liste, ancienne_valeur, nouvelle_valeur):
    for i in range(len(liste)):
        if isinstance(liste[i], list):
            modifier_occurrences(liste[i], ancienne_valeur, nouvelle_valeur)
        elif liste[i] == ancienne_valeur:
            liste[i] = nouvelle_valeur

list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
modifier_occurrences(list1, 58, 5800)
print(list1)
