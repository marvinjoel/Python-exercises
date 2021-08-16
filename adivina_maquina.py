import random, time


#Reglas para el Juego
def Regla_Juego():
    print('============================')
    print('  !Bienvenido al Juego!     ')
    print('============================\n')
    print('El juego consiste en lo siguiente:\nIngrese un número del 1 al 10\nLa computadora intentara adivinar en 3 oportunidades\n\n')

#Validación de numero entrante
def Validacion(opcion):
      fin = False
      while not fin:
            try:
                  opc = int(input(opcion))
            except ValueError:
                  print('ERROR: Ingrese solo valores numericos.\n')
            else:
                  fin = True
      return opc


def Numero_Adivinar():
    Regla_Juego() #Llamara a la funcion al ejecutarce,
    num = Validacion('Ingrese Número: ') #la funcion de VALIDAR recibe un parametro

    #For dara las oportunidades que adivinara la máquina(tambien podemos hacerlo dinamicamente)
    for x in range(3):
        maquina = random.randint(1,10)

        time.sleep(2.5)
        if num == maquina:
            print(f'La máquina adivino el valor {maquina}')
            return True
        else:
            print(f'Tú numero ingresado es: {maquina}')
            print(f'Oportunidad {x+1} fallida :(\n')
    print(':( No pude adivinar tu valor ingresado')
        
Numero_Adivinar()
