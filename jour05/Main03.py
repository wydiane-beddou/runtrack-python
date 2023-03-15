def draw_rectangle(n):

    
    print("+" + "-" * (n-2) + "+")
    # Dessine la première ligne du rectangle 
    # avec des tirets et des barres verticales
    
    for i in range(n-2):
    
        print("|" + "#" * (n-3-i) + " " + "#" * i + "|")
    # Dessine les lignes du milieu 
    # avec des # et des espaces
    
    print("+" + "-" * (n-2) + "+")
    # Dessine la dernière ligne du rectangle 
    # avec des tirets et des barres verticales

draw_rectangle(10)
# Exemple d'utilisation