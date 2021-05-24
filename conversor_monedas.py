def conv(tipo,valor):
    monto=float(input('Porfavor ingresa el monto: '))
    cantidad= round(monto / valor,2)
    print('La cantidad de pesos '+tipo+' convertidos a dolares es: '+ str(cantidad))

def run():
    menu = """
    Bienvenido al conversor de monedas...
    1.- Peso argentino
    2.- Peso colombiano
    3.- Peso boliviano

    Porfavor elija una opcion: """
    op = int(input(menu))

    if op == 1:
        conv('argentino',65)
    elif op == 2:
        conv('colombiano',1897)
    elif op == 3:
        conv('boliviano',6.96)
    else:
        print('Porfavor ingrese una opcion del menu')

if __name__=='__main__':
    run()