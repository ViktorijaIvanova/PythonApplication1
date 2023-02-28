def add_city_population(cities, population):
    while True:
        city = input("Sisestage linna nimi: ")
        people = int(input("Sisestage linna rahvaarv: "))
        cities.append(city)
        population.append(people)
        if input("Kas soovite lisada veel linna (jah/ei)? ").lower() != "jah":
            break

