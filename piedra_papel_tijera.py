import random



def Regla_Juego():
    print('============================')
    print('  !Bienvenido al Juego!     ')
    print('============================\n')
    print("El juego consiste en lo siguiente:\nLa máquina tratarra de ganarte\nTienes que escoger la opción:\nPiedra, Papel, o Tijera.\nSuerte! :)\n\n")

def Jugar():
    Regla_Juego() #Llamamos a la funcion REGLA JUEGO

    while True: 
        user = input('Ingrese la opcion: ').lower()
        lista = ['piedra','papel','tijera']
        maquina = random.choice(lista)

        if user in lista: #Se compara si el dato ingresado por el usuario está en la lista que asignamos
            if user == maquina: #Comparacion si la opcion elegida por el usuario es igual a la opcion elegida por la máquina
                return f'!Empate: sacaste: {user} y la saco {maquina}  :) '

            if Juego_ganado(user, maquina): #Llamaremos a la funcion JUEGO_GANADO, que tiene 2 argumentos
                return f'!Ganaste: sacaste, {user} y la saco {maquina}  :) '
            else:
                return f'Perdiste: sacaste: {user} y la saco {maquina}  :) '
        else:
            print('ERROR: Solo tienes que ingresar las opciones, piedra, papel, tijera.\n')

def Juego_ganado(jugador, oponente):#Recibe 2 parametros
    # Retornar true (verdadero) si gana el jugador.
    # Piedra gana a tijera (pi > ti)
    # tijera gana a papel (ti > pa)
    # papel gana a piedra (pa > pi)
    if ((jugador=='piedra' and oponente=='tijera') or (jugador=='tijera' and oponente=='papel') or (jugador=='papel' and oponente=='piedra')):
        return True
    else:
        return False


print(Jugar())


    