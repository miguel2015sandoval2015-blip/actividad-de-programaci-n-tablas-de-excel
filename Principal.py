from Usuario import usuario
from Numero import numero
from Calculadora import calculadora
#crear usuario
nombre = input("ingrese el nombre del cliente: ")
cedula = input("ingrese la cedula del cliente: ")

usuario1 = usuario(cedula,nombre)
#creo los numeros
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

num1 = numero(num1)
num2 = numero(num2)
#crear calculadora
obj_calcu = calculadora("18/02/2026")
obj_calcu.set_tipo_operacion("division")
obj_calcu.guardar_info(usuario1)

obj_calcu.hacer_operacion(num1,num2)

obj_calcu.mostrar_tabla()

