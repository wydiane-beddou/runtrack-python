import string 

def cesar(): # fonction
    text="le soleil va disparaitre" # chaine de texte
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    #chaîne d'alphabet en combinant les lettres minuscules et majuscules 
    # en utilisant les constantes fournies par le module "string"
    shift = 3 # décale de 3 lettres dans l'alphabet

    shifted = alphabet[shift:] + alphabet[:shift] 
    #Cette variable contient l'alphabet original décalé de 3 positions 
    # vers la droite, suivi des lettres qui ont été découpées 
    # à partir du début de l'alphabet original
    
    table = str.maketrans(alphabet, shifted) 
    # Cette variable contient l'alphabet original décalé de 3 positions vers la droite, 
    # suivi des lettres qui ont été découpées à partir du début de l'alphabet original

    cesar = text.translate(table)
    # La variable "cesar" contient le message chiffré. La méthode "translate" est appelée 
    # sur la chaîne "text" en utilisant la table de traduction créée précédemment

    print(cesar)

cesar()