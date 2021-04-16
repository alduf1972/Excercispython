# Enoncé : Vous créez une petie application qui donne les horaires des trains. L'utilisateur choisira sa destination et la période à laquelle il veut partir et votre application
# donnera l'heure du train. Concrètement le résultat devra ressembler à ceci :

# 1 - Bruxelles
# 2 - Mons
# 3 - Nivelles
# 4 - Charleroi
# Entrez La destination que vous voulez atteindre : 3
# Bien, vous avez choisi d'aller à Nivelles.
# 1 - Matin
# 2 - Après-midi
# 3 - Soir
# Quand souhaitez vous partir ? 3
# Ok, vous avez choisi la période : Soir
# Votre train démarre à 20h00

# Les heures sont les suivantes :
# Bruxelles (Matin) : 10h33
# Bruxelles (Midi) : 14h42
# Bruxelles (Soir) : 19h02

# Mons (Matin) : 9h10
# Mons (Midi) : 13h30
# Mons (Soir) : 22h56

# Nivelles (Matin) : 5h34
# Nivelles (Midi) : 15h13
# Nivelles (Soir) : 20h00

# Charleroi (Matin) : 7h45
# Charleroi (Midi) : 12h53
# Charleroi  (Soir) : 23h02
import sys
def Destinationchoice():
    print(" 1 - bruxelles \n 2 - Mons \n 3 - Nivelles \n 4 - Charleroi ")
    _destinationchoice=int(input("quelle est votre destination, choisissez le chiffre " ))
    if _destinationchoice==1:
        _destination="Bruxelles"
    elif _destinationchoice==2:
        _destination="Mons"
    elif _destinationchoice==3:
        _destination="Nivelles"
    elif _destinationchoice==4:
        _destination="Charleroi"
    else:
        sys.exit("Erreur, la destination rentrée est incorrecte")
    print("Bien vous avez choisis de partir à "  + _destination)
    return _destination
        
def Chooseperiodoftime():
    print(" 1 - matin \n 2 - après-midi \n 3 - soir \n ")
    _timechoice=int(input("Quand souhaitez vous partir?"))
    if _timechoice==1:
        _time="matin"
    elif _timechoice==2:
        _time="après-midi"
    elif _timechoice==3:
        _time="soir"
    else:
        sys.exit("Erreur, l'heure rentrée est incorrecte")
    print("la période que vous avez choisies est :" + _time)
    return _time

def Dysplaytime(_time, _morninghour, _afternoonhour, _eveninghour):
    if _time=="matin":
        print("Votre train démarre à " + _morninghour)
    elif _time=="après-midi":
        print("Votre train démarre à " + _afternoonhour)
    elif _time=="soir":
        print("Votre train démarre à " + _eveninghour)


destination=Destinationchoice()
time=Chooseperiodoftime()
   
    
if destination=="Bruxelles":
    Dysplaytime(time, "10h33", "14h42", "19h02")
elif destination=="Mons":
    Dysplaytime(time, "09h33", "13h15", "19h54")
elif destination=="Nivelles":
        Dysplaytime(time, "07h33", "14h55", "20h54")
elif destination=="Charleroi":
        Dysplaytime(time, "09h13", "14h25", "21h54")

  













