import tkinter as ventana

def tomar_datos():
    print("datos enviados a la base de datos: ")
    
obj_ventana = ventana.Tk()
obj_ventana .title("registro del parqueadero: ")

label_nombre = ventana.Label(obj_ventana,text="Nombre usuario")
label_nombre.pack()
label_nombre = ventana.Entry(obj_ventana)
label_nombre.pack()

Button_enviar = ventana.Button(obj_ventana,text="Enviar datos: ")
Button_enviar.pack()

obj_ventana.mainloop()    
    
