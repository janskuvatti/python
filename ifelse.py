# -*- coding: cp1252 -*-
nimi = "Erkki"
salasana = "Esimerkki"
#Ohjelmassa käyttäjältä pyydetään nimi ja salasana.
nimi2=input("Anna nimi:")

#Jos nimi on väärin, tulostaa ohjelma "Nimi oli väärin.".

#Jos nimi on oikein, pyydetään salasanaa.
#Ohjelmassa käyttäjältä pyydetään nimi ja salasana.
#Jos nimi on väärin, tulostaa ohjelma "Nimi oli väärin.". Jos nimi on oikein, pyydetään salasanaa.
#Jos salasana on oikein, tulostetaan "Salasana ja nimi oli oikein!", muussa tapauksessa
#"Salasana oli väärin.". Toteuta oikeaksi nimi-salasana-pariksi Erkki ja Esimerkki. Ohjelma tulostaa toimiessaan seuraavanlaisia vastauksia:
if not nimi2 == nimi:
	print("Nimi oli väärin.")
elif nimi2 == nimi:
    sana=input("Anna salasana:")
    if not sana == salasana:
          print("Salasana oli väärin.")
    else:
        print("Salasana ja nimi oli oikein!")
        
#Kolmas esimerkki on ensimmäinen tehtävä, jossa luodaan käyttäjälle valikko.
#Käyttäjältä pyydetään luku väliltä 1-3, ja sen mukaan, mitä käyttäjä valitsee
#tulostetaan joko "Haukion kala Oy" valinnalla 1, "Metallipaja VasaraAika"
#valinnalla 2 tai "Balin palapelitehdas" valinnalla 3. Toimiessaan ohjelma tulostaa esimerkiksi seuraavaa:
yritys1="Haukion kala Oy"
yritys2="Metallipaja VasaraAika"
yritys3="Balin palapelitehdas"
valinta=int(input("Valitse kohde (1-3):"))
if valinta == 1:
        print(yritys1)
elif valinta == 2:
        print(yritys2)
else:
        print(yritys3)
eka=int(input("Anna ensimmäinen luku:"))
toka=int(input("Anna toinen luku:"))
vastaus1=int(eka+toka)
vastaus2=int(eka-toka)
vastaus3=int(eka*toka)
vastaus4=float(eka/toka)



print("(1) +\n(2) -\n(3) *\n(4) /")
valinta=int(input("Tee valinta (1-4):"))
if valinta == 1:
	print("Tulos on: ",vastaus1)
elif valinta == 2:
	print("Tulos on: ",vastaus2)
elif valinta == 3:
	print("Tulos on: ",vastaus3)
elif valinta == 4:
	print("Tulos on: ",vastaus4)
else:
	print("Valintaa ei tunnistettu.")
        


    
