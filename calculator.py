# -*- coding: cp1252 -*-
eka=int(input("Anna ensimmäinen luku:"))
toka=int(input("Anna toinen luku:"))
vastaus1=int(eka+toka)
vastaus2=int(eka-toka)
vastaus3=int(eka*toka)
vastaus4=float(eka/toka)


while True:
   print("(1) +\n(2) -\n(3) *\n(4) / \n(5) Vaihda luvut \n(6) Lopeta")
   print("Valitut luvut: ", eka, toka)
   valinta=int(input("Tee valinta (1-6): "))
   if valinta == 1:  
        print("Tulos on: ", eka + toka)
   elif valinta == 2:
        print("Tulos on: ", eka - toka)
   elif valinta == 3:
        print("Tulos on: ", eka * toka)
   elif valinta == 4:
        print("Tulos on: "), eka / toka
   elif valinta == 5:
        eka=int(input("Anna uusi ensimmäinen luku:"))
        toka=int(input("Anna uusi toinen luku:"))
   else:
        break

