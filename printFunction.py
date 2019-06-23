# -*- coding: cp1252 -*-
def tulosta(oletus = "Oletustulostus"):
    print(oletus)
def main():
    while True:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if(sana =="Lopeta"):
           break
        elif(len(sana) < 5):
           tulosta()
        else:
           tulosta(sana)
        
    
if __name__ == "__main__":
    main()
