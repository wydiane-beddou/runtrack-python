s ='abcdefghijklmnopqrstuvwxyz' *10
n = 1 #nombre de caractère dans la ligne
i = 0 #position du premier caractère
while i + n < len(s): #len = 
    print(s[i:i+n])
    i += n
    n += 1 # +1 caractère