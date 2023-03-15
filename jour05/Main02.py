# Dimensions du rectangle
width = 10   # la largeur du rectangle est de 10 caractères
height = 3   # la hauteur du rectangle est de 3 lignes

# Dessin du rectangle
for i in range(height):   
    # pour chaque ligne allant de 0 à 2
    for j in range(width):   
    # pour chaque colonne allant de 0 à 9
        if i == 0 or i == height - 1:   
    # si on est sur la première ou la dernière ligne
            print("|" if j == 0 or j == width -1 else "-", end="")   
    # si on est sur la première ou la dernière colonne, imprimer "|", 
    # sinon "-", et ne pas passer à la ligne
        
        elif j == 0 or j == width - 1:   
    # si on est sur la première ou la dernière colonne
            print("|", end="")   
    # imprimer "|", et ne pas passer à la ligne
        
        elif i == 1 and j == width - 1:  
    # si on est sur la deuxième ligne et l'avant-dernière colonne
            print("|", end="")  
    # imprimer "|", et ne pas passer à la ligne
        
        else:   # pour toutes les autres cases
            print(" ", end="")  
        # imprimer un espace, et ne pas passer à la ligne

    print()   # passer à la ligne pour la ligne suivante
