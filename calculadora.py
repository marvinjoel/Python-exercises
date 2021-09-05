# Calculadora

class Calculadora(object):

    def __init__(self):
        self.Num1 = 0
        self.Num2 = 0

    def validar(self, opcion):
        fin = False
        while not fin:
            try:
                opc = int(input(opcion))
            except ValueError:
                print('ERROR!, Ingrese solo números.')
            else:
                fin = True
        return opc

    def valores(self):
        self.Num1 = self.validar('Ingrese Primer número: ')
        self.Num2 = self.validar('Ingrese Segundo número: ')

    def suma(self):
        self.valores()
        return f"El resultado es: {self.Num1 + self.Num2}"

    def resta(self):
        self.valores()
        return f"El resultado es: {self.Num1 - self.Num2}"

    def multiplicacion(self):
        self.valores()
        return f"El resultado es: {self.Num1 * self.Num2}"

    def division(self):
        self.valores()
        try:
            return f"El resultado es: {self.Num1 / self.Num2}"
        except ZeroDivisionError:
            print('ERROR!, No puedes dividir entre 0.')


def Menu():
    print(f"""
    {'#'*3} Menu {'#'*3}
    1)  Suma
    2)  Resta
    3)  Multiplicación
    4)  División
    0)  Salir
    """)

def Main():
    fin = False
    c = Calculadora()
    while not fin:
        Menu()
        usuario = c.validar('Ingrese una opción: ')
        if usuario == 1:
            print(c.suma())
        elif usuario == 2:
            print(c.resta())
        elif usuario == 3:
            print(c.multiplicacion())
        elif usuario == 4:
            print(c.division())
        elif usuario == 0:
            print('Fin de Programa.')
            fin = True

if __name__ == '__main__':
    Main()
