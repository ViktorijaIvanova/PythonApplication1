def inimese(linnad, inimesed):
    if linnad in linnad.keys():
        return f"The population of {linnad} is {linnad[linnad]} people."
    else:
        return 'The city is not in the list.' 
def show_inf(linnad):
    sorted_tuple = sorted(linnad.items())
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
