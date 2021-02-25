def get_names(filename='cities.txt'):
    file = open(filename, 'rt')

    names = []
    for line in file:
        line_cities = line.rstrip().split(', ')
        names.extend(line_cities)
        # names = [*names, *line_cities]
        # names = names + line_cities
    file.close()
    return names


print(get_names())
