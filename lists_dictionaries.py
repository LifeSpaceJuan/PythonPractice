def run():
    my_list = [1, "Hello", True, 4.5] # Como se inicializa una lista
    my_dict = {"firstname": "Juan", "lastname": "Salazar"}  # Como se inicializa un diccionario

    super_list = [
        {"firstname": "Juan", "lastname": "Salazar"},
        {"firstname": "Leonor", "lastname": "Gañan"},
        {"firstname": "Fernando", "lastname": "Salazar"},
        {"firstname": "Sandra", "lastname": "Caicedo"},
    ]

    super_dict = {
        "naturalnums": [1,2,3,4,5],
        "integernums": [-1,0,1,2,3],
        "floatingnums": [1.1,4.5,6.5]
    }

    for key, value in super_dict.items(): # Imprime los elementos de un diccionario
        print(key, "-", value)
    
    print("\n")

    for value in range(len(super_list)): # Imprime los elementos de una lista
        print(super_list[value])

    for values in super_list:
        for key, value in values.items():
            print(f'{key}-{value}')

if __name__ == '__main__':
    run()