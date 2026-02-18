from Usuario import usuario
from Numero import numero
from Calculadora import calculadora

#crear usuario
usuario1 = usuario("1093593748","miguel" )
usuario1.imprimir_datos()

#crear numeros
num1 = numero(5)
num2 = numero(10)

obj_calcu = calculadora("18/02/2026")
obj_calcu.guardar_info(usuario)
obj_calcu.set_tipo_operacion("suma")
data = obj_calcu.hacer_operacion(num1,num2,"tipo de operacion")
obj_calcu.mostrar_tabla()
