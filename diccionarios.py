def run():
    notas = {
        'Sofi':70,
        'Chely':69,
        'Ayo':71,
    }

    for nombre, nota in notas.items():
        print('La alumna ' + nombre + ' tiene ' + str(nota) + ' puntos')

if __name__ == '__main__':
    run()