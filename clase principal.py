from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

#Creacion de motores para 2 automoviles y 2 motocicletas
motor1 = Motor("Gasolina", 120)
motor2 = Motor("Eléctrico", 200)
motor3 = Motor("Diesel", 150)
motor4 = Motor("Híbrido", 180)

#Creacion automóviles
auto1 = Automovil("Toyota", "Corolla", 2020, motor1, 4)
auto2 = Automovil("Tesla", "Model S", 2022, motor2, 5)

#Creacion de motocicletas
moto1 = Motocicleta("Yamaha", "R1", 2019, motor3, 1000)
moto2 = Motocicleta("Honda", "CBR", 2021, motor4, 600)

# Ejecutar todos los métodos asignados a cada vehiculo
auto1.encender()
auto1.abrir_maletero()
auto1.tocar_claxon()
print(auto1)
auto1.apagar()

print()

moto1.encender()
moto1.hacer_caballito()
moto1.usar_patada_arranque()
print(moto1)
moto1.apagar()
