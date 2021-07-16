class Operacion:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    def suma(self):
        return self.numero1 + self.numero2

    def resta(self):
        return self.numero1 - self.numero2

    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2 != 0: return self.numero1 / self.numero2
        return 0

    def divisio_entera(self):
        if self.numero2 != 0: return self.numero1 // self.numero2
        return 0

    def residuo(self):
        return self.numero1 % self.numero2

    def exponente(self):
        return self.numero1 ** self.numero2
    
    def mostrado(self):
        print('Operando1={}. Operando2={}'.format(self.number1,\
                                                  self. number2))


if __name__ == '__main__':
    print('Menú Operaciones Matemáticas')
    print('1) Suma\n2) Resta\n3) Multiplicación\n4) División\
           \n5) Division Entera\n6) Residuo\n7) Exponente\n8) Salir')
    opcion = '0'

    while opcion != '8':
        opcion = input('Elija una opción[1...8]: ')
        if opcion in '1234567':
            num1 = int(input('Ingrese el número 1: '))
            num2 = int(input('Ingrese el número 2: '))
        if opcion == '1':
            operacion = Operacion(num1, num2)
            print('Suma:', operacion.suma())
        elif opcion == '2':
            operacion = Operacion(num1, num2)
            print('Resta:', operacion.resta())
        elif opcion == '3':
            operacion = Operacion(num1, num2)
            print('Multiplicación:', operacion.multiplicacion())
        elif opcion == '4':
            operacion = Operacion(num1, num2)
            print('División:', operacion.division())
        elif opcion == '5':
            operacion = Operacion(num1, num2)
            print('Division Entera:', operacion.divisio_entera())
        elif opcion == '6':
            operacion = Operacion(num1, num2)
            print('Residuo:', operacion.residuo())
        elif opcion == '7':
            operacion = Operacion(num1, num2)
            print('Exponente:', operacion.exponente())
    print('Gracias por su visita!!!')