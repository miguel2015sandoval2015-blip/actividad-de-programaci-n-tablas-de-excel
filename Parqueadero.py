class parquero:
    def __init__(self,puesto,fecha_entrada,hora_entrada,hora_salida,estado):
        self.puesto = puesto
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.estado = estado

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
        self.hora_entrada = nueva_hora_salida

    def get_estado(self):
        return self.estado

    def set_estado(self,nuevo_estado):
        self.estado = nuevo_estado

    def guardar_info(self,obj_usuario):
        self.texto_tabla = self.texto_tabla


    def mostrar_tabla(self):
        print(self.texto_tabla)         


        