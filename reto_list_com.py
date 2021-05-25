#lista de todos los multiplos de 4 que a la vez son tambien multiplos de 6 y 9 hasta 5 digitos

def run():
    cant = int(input('Indica limite maximo: '))
    lista = [i for i in range (cant) if i%4==0 and i%6==0 and i%9==0]
    print(lista)

if __name__ == '__main__':
    run()