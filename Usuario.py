class usuario:
    def __init__(self,cedula,nombre):
        self.cedula = cedula
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula 

    def set_cedula(self,nueva_cedula):
        self.cedula = nueva_cedula

    def get_nombre(self):
        return self.nombre 

    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre   

    def imprimir_datos(self):
        print(f"nombre cliente : {self.nombre}")
        print(f"cedula cliente : { self.cedula}")