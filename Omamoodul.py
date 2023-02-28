def linnad():
    # Создаем пустые списки
    cities = []
    populations = []
    
    # Просим пользователя ввести количество городов
    num_cities = int(input("Введите количество городов: "))
    
    # Заполняем списки данными о городах и населении
    for i in range(num_cities):
        city = input(f"Введите название города {i+1}: ")
        population = int(input(f"Введите население города {city}: "))
        cities.append(city)
        populations.append(population)
    
    # Возвращаем заполненные списки
    return cities, populations