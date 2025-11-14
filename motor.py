'''
Se define la clase Motor
'''
class Motor:
    # Se inicializa los atributos tipo y potencia
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia

    #encapsulamiento
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self, nueva_potencia):
        self._potencia = nueva_potencia

    # Metodo de comportamiento: encender y apagar el motor
    def encender_motor(self):
        print(f"Motor {self._tipo} encendido con {self._potencia} HP.")
    def detener_motor(self):
        print(f"Motor {self._tipo} detenido.")

    # Sobrescritura del metodo str para mostrar la informacion
    def __str__(self):
        return f"Motor tipo: {self._tipo}, Potencia: {self._potencia} HP"

# Bloque principal para ejecutar el archivo
if __name__ == "__main__":
    # Se crea un objeto motor1
    motor1 = Motor("Gasolina", 120)

    # Se llama al metodo de enceder y apagar del motor
    motor1.encender_motor()
    motor1.detener_motor()
    # Se imprime el objeto motor1, lo que activa el metodo str
    print(motor1)

