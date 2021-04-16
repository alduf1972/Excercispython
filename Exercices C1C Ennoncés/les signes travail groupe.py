_signesastro= print(input("Veuillez entrer le chiffre qui correspond à votre signe astrologique:\n 1 - Belier\n2 - Taureau\n3 - Gémeaux\n4 - Cancer\n5 - Lion\n6 - Vierge\n7 - Balance\n8 - Scorpion\n9 - Sagittaire\n10 - Capricorne\n11 - Verseau\n12 - Poisson\n"))
def Astrosign():
    print(" 1 - bruxelles \n 2 - Mons \n 3 - Nivelles \n 4 - Charleroi ")
    _Astrosign=int(input("quelle est votre destination, choisissez le chiffre " ))
    if _Astrosign==1:
        _sign="bélier"
    elif _Astrosign==2:
        _sign="taureau"
    elif _Astrosign==3:
        _sign="gémaux"
    elif _Astrosign==4:
        _sign="cancer
    elif _Astrosign==5:
    	_sign="lion"
    elif _Astrosign==6:
		_sign="vierge"
	elif _Astrosign==7:
		_sign="balance"
	elif _Astrosign==8:
		_sign="scorpion"
	elif _Astrosign==9:
		_sign="sagittaire"
	elif _Astrosign==10:
		_sign="capricorne"
	elif _Astrosign=="11"
		_sitn="verseau"
	elif _Astrosign=="12"
		_sign="poissons"
    else:
        sys.exit("Erreur, la destination rentrée est incorrecte")
    print("")
    return _sign
     