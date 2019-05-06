#Kolmas tehtävä käsittelee tyyppimuunnoksia.
#Luodaan kaksi muuttujaa, joille annetaan arvoiksi 10.6411 ja "Merkkijono".
#Tee numeroarvon sisältävälle muuttujalle int()-tyyppimuunnos,
#ja kerro merkkijono kahdella. Tämän jälkeen laita ohjelmasi tulostamaan saamasi vastaukset muodossa
# -*- coding: cp1252 -*-
arvo = 10.6411
merkki = "Merkkijono"
arvo = int(arvo)
print("Kokonaislukumuunnos ei osaa pyöristää",arvo)
print("Merkkijonon kertominen tuottaa toistoa",merkki*2)
#Viope2.4
print("""Tämä on usean rivin tulostus:
Teksti on jaettu usealle riville.
Nimi:\tPetteri
Ammatti:\tKartturi""")
#Viopen mallivastaus
merkkijono = """Tämä on usean rivin tulostus:
Teksti on jaettu usealle riville."""

print(merkkijono)

print("Nimi:\tPetteri\nAmmatti:\tKartturi")
#2.5
luku1 = input("Anna ensimmäinen luku:")
luku2 = input("Anna toinen luku:")
luku1= int(luku1)
luku2= int(luku2)
tulos = luku1+luku2
print("Tulos on:", tulos)
#2.6
sana = "Hattukauppias"
sana1=sana[0:4]
sana2=sana[9:13]
sana3= sana[::-1]
print(sana1)
print(sana2)
print(sana3)
