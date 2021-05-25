def run():
    cant = int(input('Indica la cantidad de numeros naturales: '))
    expo = int(input('Indica el exponente: '))
    dic = {i:i**expo for i in range(1,cant+1) if i % 3 !=0}
    for valor,exp in dic.items(): #ME falto el .items()
        print(str(valor) + ' elevado a ' + str(expo) + ' es: ' + str(exp))

if __name__ == '__main__':
    run()