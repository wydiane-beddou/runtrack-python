L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

min_element = L[0] # Initialisation avec le premier élément de la liste
max_element = L[0]# Initialisation avec le premier élément de la liste

for element in L:
    if element< min_element:
        min_element = element
    elif element > max_element:
        max_element = element 

print(max_element,min_element)


#Ce programme parcourt tous les éléments de la liste L
# et compare chaque élément au minimum et au maximum actuels. 
# Si l'élément actuel est inférieur au minimum actuel, 
# alors cet élément devient le nouveau minimum. 
# Si l'élément actuel est supérieur au maximum actuel, 
# alors cet élément devient le nouveau maximum. 
# À la fin de la boucle, les variables min_element et max_element 
# contiennent respectivement le minimum et le maximum de la liste, 
# qui sont affichés à l'écran.