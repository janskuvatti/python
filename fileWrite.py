# -*- coding: cp1252 -*-
nimi = input("Minkäniminen tiedosto luodaan?: ")
tiedosto = open(nimi,"w")
content = tiedosto.read()
kirjoita = input("Mitä kirjoitetaan tiedostoon?: ")
tiedosto.write(kirjoita)
print("Luotiin tiedosto ", nimi, "ja siihen tallennettiin teksti: ", kirjoita)
tiedosto.close()
