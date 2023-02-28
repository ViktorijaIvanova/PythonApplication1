def get_population(city, cities):
    if city in cities.keys():
        return f'The population of {city} is {cities[city]} people.'
    else:
        return 'The city is not in the list.' 
def show_inf(cities):
    sorted_tuple = sorted(cities.items())
    return sorted_tuple
def most_pop(cities):
    big = 0
    town = ''
    for city, pop in cities.items():
        if pop > big:
            big = pop
            town = city
    return f'{town} : {big}'
def less(cities, num):
    my_dic = {}
    for city, pop in cities.items():
        if pop < num:
            my_dic[city] = pop
    return my_dic
