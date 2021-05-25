def run():
    cant = int(input('Ingresa la cantidad de numeros para calcular las raices cuadradas: '))
    dic_square = {i:i**0.5 for i in range(1,cant)}
    print(dic_square)

if __name__ == '__main__':
    run()