# -*- coding: cp1252 -*-
while True:
    print("(1) Lue muistikirjaa\n(2) Lis�� merkint�\n(3) Tyhjenn� muistikirja\n(4) Lopeta")
    valinta=int(input("Mit� haluat tehd�?: "))
    if valinta == 1:
        tiedosto = open("muistio.txt", "r")
        lue = tiedosto.read()
        print(lue)
        tiedosto.close()
    elif valinta == 2:
        tiedosto = open("muistio.txt","w")
        merkinta = input("Kirjoita uusi merkint�: ")
        tiedosto.write(merkinta)
        tiedosto.close()
    elif valinta == 3:
        tiedosto = open("muistio.txt","w")
        tiedosto.close()
        print("Muistio tyhjennetty.")	
    elif valinta == 4:
        print("Lopetetaan.")
        break
    else:
        print("Valintaa ei tunnistettu.")
