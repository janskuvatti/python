# -*- coding: cp1252 -*-
def laskePotenssi(numero):
    tulos = numero**2
    print("Toinen potenssi on ", tulos)
    return tulos
    
def main():
    luku = int(input("Anna lukuarvo: "))
    laskePotenssi(luku)
if __name__ == "__main__":
    main()
