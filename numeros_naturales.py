def run():
    cant=int(input('Introduce la cantidad de numeros naturales: '))
    exp=int(input('Indica la potencia a elevar por cada numero natural: '))
    resultados = []
    no_div_3 = []
    no_div3 = []
    for i in range(1,cant):
        res_exp = i ** exp
        print(str(i) + ' elevado a la potencia ' + str(exp) + ' es igual a: ' + str(res_exp))
        resultados.append(res_exp)
        if (res_exp) % 3 != 0:
            no_div_3.append(res_exp)
        if i % 3 != 0:
            no_div3.append(res_exp)
    print(resultados)
    print('nos resultados no divisibles entre 3 son: ')
    print(no_div_3)
    print(no_div3)
if __name__=='__main__':
    run()