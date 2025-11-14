from vehiculo import Vehiculo

''' 
Clase hija - Automovil
'''

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, numero_puertas):
        super().__init__(marca, modelo, anio, motor)
        self.numero_puertas = numero_puertas

    # Métodos de comportamiento
    def abrir_maletero(self):
        print(f"{self.marca} {self.modelo}: Maletero abierto.")

    def tocar_claxon(self):
        print(f"{self.marca} {self.modelo}: ¡Beep beep!")

    # Sobrescritura de __str__ usando super()
    def __str__(self):
        return super().__str__() + f", Puertas: {self.numero_puertas}"