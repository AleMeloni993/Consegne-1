# scrivo un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche

print ("Calcolo del perimetro di figure geometriche")

print("Scegli una figura a piacere tra queste : ")

print("1. Quadrato")

print("2. Cerchio")

print("3. Rettangolo")

print("4. Esci")

while True:

    scelta = input("Inserisci il numero della figura scelta : ")

    if scelta == "1":          #QUadrato : perimetro = lato * 4
        
        lato = int(input("Inserisci la lunghezza del lato : "))
        
        perimetro = lato * 4
        
        print(f"Il perimetro del quadrato è : {perimetro}")
        
    elif scelta == "2":         #Cerchio : circonferenza = 2*3.14*raggio
        
        raggio = int(input("Inserisci la lunghezza del raggio : "))
        
        circonferenza = 2*3.14*raggio
        
        print(f"La circonferenza del cerchio è : {circonferenza}")
        
    elif scelta == "3":         #Rettangolo : perimetro = base*2 + altezza*2
        
        base = int(input("Inserisci la lunghezza della base : "))
        
        altezza = int(input("Inserisci la misura dell'altezza : "))
        
        perimetro = base*2 + altezza*2
        
        print(f"Il perimetro del rettangolo è : {perimetro} ")
        
    elif scelta == "4":
        
        print("Ferma il programma")
        
        break
        
    else:
        
        print("La tua scelta non è valida, riprova!")
    
    
    
    
    
    
    
    