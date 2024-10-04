

class Calculadora:

    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    
calculadora = Calculadora()

print(calculadora.sumar(2, 3))
print(calculadora.restar(2, 3))
print(calculadora.multiplicar(2, 3))
print(calculadora.dividir(2, 3))