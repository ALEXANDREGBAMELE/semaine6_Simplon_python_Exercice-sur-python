#Exercice 2
#Calcul de factoriel
def calcul_factoriel(nombre) :
    if nombre == 0 or nombre == 1:
        return 1
    else:
        resultat = 1
        for i in range(2,nombre) : 
            resultat *= i 
        return resultat 
    
nombre = int(input("entrer un nombre : "))
factorielle = calcul_factoriel(nombre)
print(f"La factorielle de {nombre}! est {factorielle}")