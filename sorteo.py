import random

def sorteo(participantes,ganadores):
    #ganador = random.choice(participantes)
    #return ganador
    lista = []
    for i in range(ganadores):
        indice = random.choice(participantes)
        lista.append(indice)
        #participantes.pop(indice)
    for nombre in lista:
        print(nombre)

def run():
    cant = int(input('Introduce la cantidad de participantes: '))
    ganadores = int(input('Indroduce la cantidad de ganadores: '))
    participantes = []
    for i in range(cant):
        participante = input('introduce el nombre del participante nro: ' + str(i+1) + ': ')
        participantes.append(participante)
    print('los ganadores sorteados son: ')
    sorteo(participantes,ganadores)
    #print('El ganador del sorteo es: ' + sorteo(participantes))

if __name__ == '__main__':
    run()