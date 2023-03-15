def calcule():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    sum_pairs = 0 # initialisation de la variable
    for num in L:
        if num % 2 == 0:
            sum_pairs += num # somme des paires += addition

    print(sum_pairs) # afficher la somme
calcule()
