from Usuario import usuario
from Carro import carro
from Parqueadero import parqueadero
from datetime import datetime

#datos del cliente
nombre = input("ingrese el nombre del usuario: ")
cedula = input("ingrese la cedula del usuario: ")
tipo_cliente = ("ingrese tipo de cliente: ")

usuario1 = usuario(nombre,cedula,tipo_cliente)

#DATOS DEL VEHICULO
placa = input("digite la placa de su vehiculo: ")
tipo = input("digite el tipo de vehiculo (SEDAN/SUV/HATCHBACK/PICKUP): ")
color = input("digite el color de su vehiculo: ")

carro1 = carro(placa,tipo,color)

#DATOS DE PARQUEADERO
obj_parqueadero = parqueadero()

puesto = int(input("ingrese el numero del parqueadero: "))
obj_parqueadero.set_puesto = (puesto)
obj_parqueadero.registrar_entrada(usuario1,carro1)
obj_parqueadero.guardar_info()

obj_parqueadero.mostrar_tabla

registrar_salida = input("¿quiere digitar la salida de su vehiculo [si/no]: ")

if registrar_salida.lower() == "si":
    placa = input("ingrese la placa de su vehiculo para poder salir del parqueadero: ")
    
    obj_parqueadero.registrar_salida(placa)
    obj_parqueadero.guardar_info()

obj_parqueadero.mostrar_tabla()    