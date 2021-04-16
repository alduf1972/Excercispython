def Sum(_nbr1,_nbr2):
    return _nbr1+_nbr2

def Substraction(_nbr1,_nbr2):
    return _nbr1-_nbr2

def Multiplication(_nbr1,_nbr2):
    return _nbr1*_nbr2

def Division(_nbr1,_nbr2):
    return _nbr1/_nbr2

def Square(_nbr):
    return _nbr*_nbr

def GiveEveryResult(_nbr1,_nbr2):
    print("The result of the Sum of " + str(_nbr1) + " and " + str(_nbr2) +  " is " + str(Sum(_nbr1,_nbr2)))
    print("The result of the Substraction of " + str(_nbr1) + " and " + str(_nbr2) +  " is " + str(Substraction(_nbr1,_nbr2)))
    print("The result of the Division of " + str(_nbr1) + " and " + str(_nbr2) +  " is " + str(Multiplication(_nbr1,_nbr2)))
    print("The result of the Multiplication of " + str(_nbr1) + " and " + str(_nbr2) +  " is " + str(Division(_nbr1,_nbr2)))
    print("The result of the Square of " + str(_nbr1) + " is " + str(Square(_nbr1)) + " and the result of the Square of " + str(_nbr2) + " is " + str(Square(_nbr2)))
          
print("Entrez deux nombres, je ferai une série d'opération avec.")

GiveEveryResult(int(input("Entrez le premier nombre :\n")),int(input("Entrez le deuxième nombre :\n")))

