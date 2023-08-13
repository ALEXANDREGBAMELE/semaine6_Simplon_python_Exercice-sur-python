# Exercice 5 : 
# Afficher les nombres d’une liste qui sont divisibles par 5

liste_nombres = [10, 25, 7, 30, 45, 8, 15, 20, 50]

nombres_divisibles_par_5 = [nombre for nombre in liste_nombres if nombre % 5 == 0]

print("Nombres divisibles par 5 :", nombres_divisibles_par_5)