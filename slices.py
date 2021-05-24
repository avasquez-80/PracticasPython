def palindromo(txt):
    txt = txt.strip().lower().replace(' ','')
    inv = txt[::-1]
    if txt == inv:
        return True
    else:
        return False

def contar(letra,txt):
    c=0
    for caracter in txt:
        if caracter.lower() == letra:
            c+=1
    print('la cantidad de letras '+letra+' en la cadena es de: '+ str(c))

def run():
    txt = input('Porfavor ingresa un texto: ')
    if palindromo(txt):
        print('El texto ingresado es palindromo')
    else:
        print('El texto ingresado no es palindromo')
    
    letra = input('Cual es la letra que deseas contar?')
    contar(letra,txt)

if __name__=='__main__':
    run()