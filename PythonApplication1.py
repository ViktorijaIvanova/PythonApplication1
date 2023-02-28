from Omamoodul import*
cities = []
populations = []
while True:
        city = input('Введите название города. ')
        population = int(input('Введите население этого города. '))
        cities.append(city)
        populations.append(population)
        escape = input('Введите "q" для завершения ввода данных о городах \
        или Enter для продолжения. ')
        if escape.lower() == 'q':
            break
city_dict = dict(zip(cities, populations))
while True:
    command = input('Команды: 1, 2, 3, 4, q ')
    if command == '1':
        city = input('Введите название города. ')
        print(get_population(city, city_dict))
    if command == '2':
        print(show_inf(city_dict))
    if command == '3':
        print(most_pop(city_dict))
    if command == '4':
        num = int(input('Введите количество населения. '))
        print(less(city_dict, num))
    if command == 'q':
        break
