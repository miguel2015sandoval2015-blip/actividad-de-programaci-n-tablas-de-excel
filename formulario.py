import tkinter as formulario

def tomar_datos():
    print ("Datos enviados a la base de datos: ")
    
obj_formulario = formulario.Tk()
obj_formulario.title("resgistro de numeros") 
#para crear el primer numero
label_nombre = formulario.Label(obj_formulario,text="Digite el primer número")
label_nombre.pack()
entry_numero = formulario.Entry(obj_formulario)
entry_numero.pack()   
#para crear el segundo numero a sumar
label_nombre = formulario.Label(obj_formulario,text="Digite el segundo número")
label_nombre.pack()
entry_numero = formulario.Entry(obj_formulario)
entry_numero.pack()
#para crear el boton que dice enviar datos
button_enviar = formulario.Button(obj_formulario,text="Enviar numeros")
button_enviar.pack()

obj_formulario.mainloop()
