import random


#Reglas para el Juego
def Regla_Juego():
    print('============================')
    print('  !Bienvenido al Juego!     ')
    print('============================\n')
    print('El juego consiste en lo siguiente:\nTienes que adivinar el\nNumero random del 1 al 10 \nSolo tienes 4 oportunidades\n\n')
    
#Validación de numero entrante
def Validacion(opcion):
    fin = False
    while not fin:
        try:
            opc = int(input(opcion))
        except ValueError:
            print('ERROR: Ingrese solo Números.\n')
        else:
            fin = True
    return opc
    
def Adivina_numero():
    Regla_Juego() #Llamara a la funcion
    num = 4

    while num !=0: #Mientra la variable num sea diferente a 0, ingresara al bucle
        n_aleatorio = random.randint(1,10)
        n_elegir = Validacion('Ingrese numero: ') #La funcion VALIDACION recibe un parametro
        if n_aleatorio == n_elegir:
            print(f'Felicidades!, adivinaste el número: {n_aleatorio}')
            break
        else:
            if num == 2:
                print(':( Le queda una Ultima oportunidad, Suerte.')
            elif num == 1:
                print(':( Sorry, Fallaste')
                break
        num -= 1
        print(f'Te quedan {num} oportunidades\n')

Adivina_numero()