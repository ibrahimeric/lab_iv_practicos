"""  4- Implementa una clase en Python que modele una 
cuenta bancaria, con métodos para depositar, 
retirar y consultar saldo. """

class cuenta_bancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Saldo actual: ${self.saldo}"
        else:
            return "La cantidad a depositar debe ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro exitoso. Saldo actual: ${self.saldo}"
        elif cantidad > self.saldo:
            return "Fondos insuficientes para realizar el retiro."
        else:
            return "La cantidad a retirar debe ser mayor que cero."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.saldo}"

# Ejemplo de uso
saldo = int(input('Saldo actual: ')) #Ingresa el saldo en la cuenta
cuenta = cuenta_bancaria(saldo)  # Crear una cuenta con saldo inicial
print(cuenta.consultar_saldo())  # Consultar saldo
print(cuenta.depositar(500))  # Depositar $500
print(cuenta.retirar(200))  # Retirar $200
print(cuenta.consultar_saldo())  # Consultar saldo nuevamente