import requests


class Dolar:
    def __init__(self):
        self.__Url = 'https://deperu.com/api/rest/cotizaciondolar.json'

    def Request(self):
        #Traer datos de la URL
        r = requests.get(self.__Url)
        datos = r.json()
        return datos

    def Validacion(self, opcion):
        #Validacion de opcion, solo números
        fin = False
        while not fin:
            try:
                opc = int(input(opcion))
            except ValueError:
                print('ERROR: Solo ingrese valores numericos.')
            else:
                fin = True
        return opc

    def TraerDatos(self):
        sitio = self.Request()['sitio']
        enlace = self.Request()['enlace']
        precio_dolar = float(self.Request()['Cotizacion'][0]['Venta'])
        precio_dolar_c = float(self.Request()['Cotizacion'][0]['Compra'])

        print('################')
        print('Cambio de Dolar')
        print('################')

        print(f'\nDe: {sitio}')
        print(f'Url: {enlace}')

        print('\nTipo de cambio Dolar:')
        print(f'Venta: S/{precio_dolar:.2f}')
        print(f'Compra: S/{precio_dolar_c:.2f}')

        while True:
            print("""
            Opción:
            
            1) Cambio de Dolares a Soles.
            2) Cambio de Soles a Dolares.
            3) Salir
            """)
            usuario = self.Validacion('que tipo de cambio desea realizar?: ')
            if usuario == 1:
                dolares = float(input('\nIngrese su valor en Dolares: '))
                r = precio_dolar * dolares
                print(f'El cambio en Soles es: S/{r:.2f}\n')
            elif usuario == 2:
                dolares = float(input('\nIngrese su valor en Soles: '))
                r = dolares / precio_dolar
                print(f'El Cambio en Dolares es: ${r:.2f}\n')
            elif usuario == 3:
                print('Hasta luego.')
                break


if __name__ == '__main__':
    dolar = Dolar()
    dolar.TraerDatos()
