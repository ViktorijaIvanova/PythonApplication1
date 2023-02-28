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
    käsk = input("käsk:1-Uurige linna nime sisestades, kui palju elanikke selles on/ 2-tähestikuline linnade loetelu ja elanike arv/ 3-Sisestage elanike arv ja kuvage linna nimi, kus on lähim elanikke/ 4-Leidke linnad, kus on vähem kui n elanikku")
    if käsk == "1":
        city = input("sisetage nimi linnas:")
        print(inimesed(linnad,linnas_dict ))
    if käsk == "2":
        print(show_inf(linnas_dict))
    if käsk == "3":
        print(most_pop(linnas_dict))
    if käsk == "4":
        num = int(input("Sisesta rahvaarv:"))
        print(less(linnas_dict, num))
    if käsk == 'q':
        break
