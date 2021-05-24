import random
import os

def run():
    menu = """ Adivina el numero
    
    3.- Facil (9 oportunidades)
    2.- Medio (6 oportunidades)
    1.- Dificil (3 oportunidades)
    
    Indica el nivel al que deseas competir:  """
    
    vueltas = int(input(menu)) * 3
    tope = int(input('Ingresa el limite superior a adivinar: '))
    rand = random.randint(0,tope)
    win = False

    numero = int(input('Ingresa un numero: '))
    for i in range(1,vueltas):
        if numero == rand:
            os.system('clear')
            print('Felicidades!!! ganaste el juego')
            win = True
            break
        elif numero < rand:
            print('Fallaste, tienes ' + str(vueltas-i)+' oportunidades mas')
            numero = int(input('El numero ingresado es menor al calculado por la PC, intenta subiendo un poco: '))
            os.system('clear')
        elif numero > rand:
            print('Fallaste, tienes ' + str(vueltas-i)+' oportunidades mas')
            numero = int(input('El numero ingresado es mayor al calculado por la PC, intenta bajando un poco: '))
            os.system('clear')
    if win == False:
        
        print('Ni modo perdiste, vuelve a intentarlo (talvez en un nivel mas facil)')            

if __name__ == '__main__':
    run()