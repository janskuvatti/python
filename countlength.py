# -*- coding: cp1252 -*-
def laskePituus(merkkijono):
    pituus = len(merkkijono)
    if(pituus == 0):
        print("Et antanut sy�tett�")
    else:
        print("Antamasi sy�te oli", pituus, " merkki� pitk�.")
    return pituus
def main():
    while True:
        sana = input("Anna sy�te (Lopeta lopettaa): ")
        if(sana == "Lopeta"):
            break
       
        laskePituus(sana)
        
        
    
if __name__ == "__main__":
    main()
