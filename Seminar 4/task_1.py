def filter_data(lst):
    return len(list(filter(lambda x: x[1] >= 30, lst)))


init_list = ([('Max', 41), ('Andrey', 25), ('Victor', 42), ('Ivan', 35)])
print(filter_data(init_list))
