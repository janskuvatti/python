# -*- coding: cp1252 -*-
nimi = input("Mink�niminen tiedosto luodaan?: ")
tiedosto = open(nimi,"w")
content = tiedosto.read()
kirjoita = input("Mit� kirjoitetaan tiedostoon?: ")
tiedosto.write(kirjoita)
print("Luotiin tiedosto ", nimi, "ja siihen tallennettiin teksti: ", kirjoita)
tiedosto.close()
