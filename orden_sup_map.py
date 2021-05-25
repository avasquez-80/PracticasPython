from functools import reduce #para poder usar la funcion reduce
def run():
    lista = [1,2,3,4,5]
    
    lista2 = [2,2,2,2,2]
    
    #list_square = [i**2 for i in list]
    list_square = list(map(lambda i:i**2,lista)) #no olvidar lambda y usar un nombre de lista diferente a list
    list_impar = list(filter(lambda i:i%2!=0,lista))
    
    x = 1
    for i in lista2:
        x*=i

    y = reduce(lambda a,b:a*b,lista2) # funcion reduce primer iteraccion a viene a ser el indice 0 y b el indice 1, segunda iteraccion el resultado de la primera operando al indice 2

    print(lista)
    print(list_square)
    print(list_impar)

    print(x)
    print(y)

if __name__ == '__main__':
    run()