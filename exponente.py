def exponente(base,potencia):
    exp = 0
    resultado = 0
    while exp <= potencia:
        resultado = base ** exp #aqui le estaba pelando 
        exp+=1
    return resultado

def run():
    base = int(input('Introduce la base: '))
    potencia = int(input('Introduce la potencia: '))
    print('El resultado de la operacion es: ' + str(exponente(base,potencia)))

if __name__ == '__main__':
    run()