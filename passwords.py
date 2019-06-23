# -*- coding: cp1252 -*-
tiedosto = open("merkkijonoja.txt","r")
rivi = ""
while True:
    
    rivi = tiedosto.readline()
    
    if rivi == "":
        break
    rivi = rivi[:-1]
    if rivi.isalnum() == False:
        print(rivi, " sisältää virheellisiä merkkejä.")
    else:
        print(rivi, " kelpaa salasanaksi.")
    
tiedosto.close()
