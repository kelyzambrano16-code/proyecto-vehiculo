from vehiculo import Vehiculo

'''
Clase hija -  Motocicleta
'''
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, motor, cilindraje):
        super().__init__(marca, modelo, anio, motor)
        self.cilindraje = cilindraje

    # Métodos de comportamiento
    def hacer_caballito(self):
        print(f"{self.marca} {self.modelo}: ¡Caballito en acción!")
    def usar_patada_arranque(self):
        print(f"{self.marca} {self.modelo}: Patada de arranque usada.")

    # Sobrescritura de __str__ usando super()
    def __str__(self):
        return super().__str__() + f", Cilindraje: {self.cilindraje} cc"
