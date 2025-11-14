'''
Se define Super Clase  Vehiculo
'''
class Vehiculo:
    def __init__(self, marca, modelo, anio, motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor  # Composición: motor es un objeto

    # Encapsulamiento
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    @property
    def anio(self):
        return self._anio
    @anio.setter
    def anio(self, nuevo_anio):
        self._anio = nuevo_anio

    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, nuevo_motor):
        self._motor = nuevo_motor

    # Métodos de comportamiento encender y apagar
    def encender(self):
        print(f"{self._marca} {self._modelo} encendido.")
        self._motor.encender_motor()

    def apagar(self):
        print(f"{self._marca} {self._modelo} apagado.")
        self._motor.detener_motor()

    # Mostrar información del vehículo
    def __str__(self):
        return f"{self._marca} {self._modelo} ({self._anio}) con {self._motor}"