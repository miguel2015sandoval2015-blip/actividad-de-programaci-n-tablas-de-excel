class usuario:
    def __init__(self,nombre,cedula):
        self.nombre = nombre
        self.cedula = cedula
        
    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,nueva_cedula):
        self.cedula = nueva_cedula  
        
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def imprimir_datos(self):
        print(f"nombre de cliente es : {self.nombre}")
        print(f"cedula de cliente es : {self.cedula}")          