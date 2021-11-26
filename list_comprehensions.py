def run():
    """ squares = []

    for i in range(1, 100):
        if i % 3 != 0:
            squares.append(i**2)
    print(squares) """

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    reto_list = [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(reto_list, "\n")

    reto_lists = [i for i in range(1, 100000) if i % 36 == 0]
    print(reto_lists)

if __name__ == '__main__':
    run()