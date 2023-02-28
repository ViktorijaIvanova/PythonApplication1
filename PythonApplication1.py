from Omamoodul import*
linnad = []
inimesed= []
while True:
        linn = input("Sisetage nimi linnas:" )
        inimes = int(input("sisetage inimesed sest linnas:" ))
        linn.append(linnad)
        inimes.append(inimesed)
        väljuda=input("sisetage  "o" linnaandmete sisestamise lõpetamiseks \või jätkamiseks vajutage sisestusklahvi:")
        if väljuda.lower() == "o":
            break
linnas_dict = dict(zip(linnad, inimesed))
while True:
    käsk = input("käsk:1-Uurige linna nime sisestades, kui palju elanikke selles on/ 2-tähestikuline linnade loetelu ja elanike arv/ 3-Sisestage elanike arv ja kuvage linna nimi, kus on lähim elanikke/ 4-Leidke linnad, kus on vähem kui n elanikku/ 5-otsi esimese tähe järgiю")
    if käsk == "1":
        linn = input("sisetage nimi linnas:")
        print(inimesed(linn,linnas_dict ))
    if käsk == "2":
        print(show_inf(linnas_dict))
    if käsk == "3":
        print(most_pop(linnas_dict))
    if käsk == "4":
        number= int(input("Sisesta rahvaarv:"))
        print(less(linnas_dict, number))
    if käsk== "5":
        täht=input("sisetage esimene täht:")
        sõna= [sõna for sõna in linnad if sõna.startswith(täht)]
        print(sõna)
    if käsk == "o":
        break
