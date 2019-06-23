# -*- coding: cp1252 -*-
def laskePituus(merkkijono):
    pituus = len(merkkijono)
    if(pituus == 0):
        print("Et antanut syötettä")
    else:
        print("Antamasi syöte oli", pituus, " merkkiä pitkä.")
    return pituus
def main():
    while True:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if(sana == "Lopeta"):
            break
       
        laskePituus(sana)
        
        
    
if __name__ == "__main__":
    main()
