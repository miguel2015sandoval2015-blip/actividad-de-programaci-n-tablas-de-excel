from datetime import datetime

class parqueadero:
    def __init__(self):
        self.puesto = None
        self.fecha_entrada = None
        self.hora_entrada = None
        self.hora_salida = None
        self.estado = "libre"
        self.cliente = None
        self.carro = None
        self.texto_tabla = ""

    def get_puesto(self):
        return self.puesto

    def set_puesto(self,nuevo_puesto):
        self.puesto = nuevo_puesto

    def get_fecha_entrada(self):
        return self.fecha_entrada

    def set_fecha_entrada(self,nueva_fecha):
        self.fecha_entrada = nueva_fecha

    def get_hora_entrada(self):
        return self.hora_entrada

    def set_hora_entrada(self,nueva_hora_entrada):
        self.hora_entrada = nueva_hora_entrada

    def get_hora_salida(self):
        return self.hora_salida

    def set_hora_salida(self,nueva_hora_salida):
        self.hora_salida = nueva_hora_salida

    def get_estado(self):
        return self.estado

    def set_estado(self,nuevo_estado):
        self.estado = nuevo_estado
        
        
    def registrar_entrada(self,cliente,carro):
        self.cliente = cliente
        self.carro = carro
        ahora = datetime.now()
        self.fecha_entrada = ahora.date()
        self.hora_entrada = ahora.time()
        self.estado = "ocupado"
            
    def registrar_salida(self,placa_buscar):
        if self.estado == "ocupado" and self.carro.get_placa() == placa_buscar:
            
            hora = datetime.now()
            self.hora_salida = hora.time()
            self.estado = "libre"
    
    def guardar_info(self):
        self.texto_tabla += f"Puesto: {self.puesto}\n"
        self.texto_tabla += f"estado: {self.estado}\n"
        self.texto_tabla += f"fecha entrada: {self.fecha_entrada}\n"
        self.texto_tabla += f"hora entrada: {self.hora_entrada}\n"
        self.texto_tabla += f"cliente: {self.cliente.get_nombre_usuario()}\n"
        self.texto_tabla += f"cedula: {self.cliente.get_cedula_usuario()}\n"
        self.texto_tabla += f"placa: {self.carro.get_placa()}\n"
        self.texto_tabla += f"tipo vehiculo {self.carro.get_tipo()}\n"

    def mostrar_tabla(self):
        print(self.texto_tabla)         


        