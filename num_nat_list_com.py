def run():
    cant=int(input('Introduce la cantidad de numeros naturales: '))
    exp=int(input('Indica la potencia a elevar por cada numero natural: '))
    resultados = [i**exp for i in range (1,cant) if i % 3 != 0]
    print(resultados)

if __name__ == '__main__':
    run()