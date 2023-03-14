def code(langage):
    if langage == 'javascript':
       return ("tu es developpeur web")
    elif langage == 'python':
       return ("tu es un developpeur IA")
    elif langage == 'java':
      return ("tu es un developpeur logiciel")
    else :
       return ("tu es un developpeur mobile")

langage ='python'
print(code(langage))