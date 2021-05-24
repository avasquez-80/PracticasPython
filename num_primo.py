def primo(numero):
    pri=1
    for c in range(1,numero):
        if numero % c == 0:
            pri +=1
    if pri > 2:
        return False
    else:
        return True

def run():
    primos=[]
    limite = int(input('Ingresa el limite superior: '))
    for i in range(2,limite):
        if primo(i):
            primos.append(i)
    print(primos)

if __name__ == '__main__':
    run()