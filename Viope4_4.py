  # -*- coding: cp1252 -*-
eka=int(input("Anna ensimmäinen luku:"))
toka=int(input("Anna toinen luku:"))
vastaus1=int(eka+toka)
vastaus2=int(eka-toka)
vastaus3=int(eka*toka)
vastaus4=float(eka/toka)
print("(1) +\n(2) -\n(3) *\n(4) /\n(5) Vaihda luvut\n(6) Lopeta")

valinta=int(input("Tee valinta (1-6):"))

if valinta == 1:
    print("Tulos on: ",vastaus1)
elif valinta == 2:
    print("Tulos on: ",vastaus2)
elif valinta == 3:
    print("Tulos on: ",vastaus3)
elif valinta == 4:
    print("Tulos on: ",vastaus4)
    
    elif valinta == 5:
            eka=int(input("Anna ensimmäinen luku:"))
            toka=int(input("Anna toinen luku:"))
    else:
	    print("Valintaa ei tunnistettu.")
	
#elif valinta == 6:
    #break




    

