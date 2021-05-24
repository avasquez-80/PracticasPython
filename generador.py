import random

def contracena(cant_car):
    mayusc = ['A','B','C','D','E','F']
    minusc = ['a','b','c','d','e','f']
    numeros = ['1','2','3','4','5','6','7','8','9']
    caracteres = ['#','$','%','&','(',')','!','@']

    car = mayusc + minusc + numeros + caracteres
    password = []

    for i in range(cant_car):
        car_random = random.choice(car)
        password.append(car_random)

    password = ''.join(password) #Convertir lista a string
    return password

def run():
    cant_car = int(input('ingresa la cantidad de caracteres para tu contracena: '))
    print('tu contracena es: ' + contracena(cant_car))

if __name__ == '__main__':
    run()