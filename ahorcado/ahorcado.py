from listas import palabras, vidas_diccionario_visual

import random, string



def Ahorcado():
    print("===================================")
    print('¡Bienvenid@ al juego del Ahoracado!')
    print("===================================")

    palabra = random.choice(palabras).upper()

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar)> 0 < vidas:

        if vidas !=1 and vidas !=7:
            print(f"Te quedan {vidas} vidas y has usado estas letras: {'-'.join(letras_adivinadas)}")
        elif vidas ==7:
            if len(letras_adivinadas)>0:
                print(f"Te quedan {vidas} vidas, y has usado estas letras: {'-'.join(letras_adivinadas)}")
            else:
                print(f"Te quedan {vidas} vidas, a jugar, ¡Suerte!..: {'-'.join(letras_adivinadas)}")
        else:
            print(f"Te queda {vidas} vida y has usado estas letras: {'-'.join(letras_adivinadas)}")

        palabra_lista = [ letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostrar al ahoracado
        print(vidas_diccionario_visual[vidas])
        #Mostrar las letras separadas por un espacio
        print(f"Plabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        #Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresado
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            #Si la letra esta en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        #Si la letra escogida por el usuario ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva")
        else:
            print("\nEsta letra no es valida")

    #El juego llega a esta línea cuando se adivina todas las letras de la palabra o cuando se termina las vidas del jugador
    if vidas ==0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. la palabra era: {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")

Ahorcado()