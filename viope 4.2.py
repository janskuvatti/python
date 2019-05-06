  # -*- coding: cp1252 -*-
#teksti = "Kirjoita jotain: "
loppu = "Lopetit ohjelman."
lopetus = "lopeta"
sana = input("Kirjoita jotain: ")

while not sana == lopetus:
    print(sana)
    sana = input("Kirjoita jotain: ")
    if sana == lopetus:
        print(loppu)


