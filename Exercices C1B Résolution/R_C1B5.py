# Enoncé : Créez d'abord 2 fonctions. Une qui va écrire l'âge, et une qui va écrire la date de naissance
# (avec une petite phrase qui accompagne du style "Vous avez X ans")
# de la personne qui appelle la fonction. La première fonction prend en paramètre l'âge, la deuxième prend
# en paramètre la date de naissance en chaîne de caractère.
# Appelez ces deux fonctions pour que cela affiche d'abord l'âge puis la date de naissance de la personne

# Maintenant le réel exercice Au seul appel d'une fonction (vous pouvez en recréer si vous voulez), l'âge 
# Et la date de naissance de la personne seront affichés. Il y a trois solutions possibles, essayez de les
# trouver !

#region indice
# La première est la plus simple, il suffit dans cette fonction de réécrire ce qu'il se passe dans les
# deux fonctions précédentes, c'est la plus "mauvaise" solution. Dans l'absolu, mais la meilleur dans ce cas
#endregion

#region indice
# La deuxième solution est, depuis cette troisième fonction, d'appeler les deux autres fonctions,
# C'est la solution la plus classique et la meilleure
#endregion

#region indice
# La troisème solution est de faire en sorte que depuis la première fonction, on appelle la deuxième
#endregion

def TellAge(_age):
    print ("Vous avez " + _age + "ans.")
    
def TellBirthDate(_birthDate):
    print("Vous êtes né le " + _birthDate)
    
TellAge("27")
TellBirthDate("25/04/9393")

# Solution 2 :

def TellAge2(_age,_birthDate):
    print ("Vous avez " + _age + "ans.")
    TellBirthDate(_birthDate)

    
TellAge2("48","22/22/33")