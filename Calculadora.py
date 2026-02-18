class calculadora:
    def __init__(self,fecha_uso):
        self.tipo_operacion = ""
        self.resultado = ""
        self.fecha_uso = fecha_uso
        self.texto_tabla = ""
        

    def get_tipo_operacion(self):
        return self.tipo_operacion

    def set_tipo_operacion(self,nueva_operacion):
        self.tipo_operacion = nueva_operacion    


    def get_resultado(self):
        return self.resultado
    
    def set_resultado(self,nuevo_resultado):
        self.resultado = nuevo_resultado

    def get_fecha_uso(self):
        return self.fecha_uso

    def set_fecha_uso(self,nueva_fecha):
        self.fecha_uso = nueva_fecha     

    def calcular_suma(self,obj_num1,obj_num2):
        resul_suma = obj_num1.get_numero() + obj_num2.get_numero()
        self.resultado = resul_suma
        print(f"el resultdo de la suma es: {resul_suma}")

    
    def calcular_resta(self,obj_num1,obj_num2):
        resul_resta = obj_num1.get_numero() - obj_num2.get_numero()
        self.resultado = resul_resta
        print(f"el resultdo de la resta es: {resul_resta}")

    def calcular_multi(self,obj_num1,obj_num2):
        resul_mul = obj_num1.get_numero() * obj_num2.get_numero()
        self.resultado = resul_mul
        print(f"el resultdo de la multiplicacion  es: {resul_mul}")

    def calcular_div(self,obj_num1,obj_num2):
        resul_div = obj_num1.get_numero() / obj_num2.get_numero() 
        self.resultado = resul_div
        print(f"el resultdo de la division es: {resul_div}")   


    def hacer_operacion(self, obj_num1, obj_num2, tipo_operacion):
        if self.tipo_operacion == "suma":
            self.resultado = self.calcular_suma(obj_num1.get_numero(), obj_num2.get_numero())
            return self.resultado
        elif self.tipo_operacion == "resta":
            self.resultado = self.calcular_resta(obj_num1.get_numero(), obj_num2.get_numero())
            return self.resultado
        elif self.tipo_operacion == "multiplicacion":
            self.resultado = self.calcular_multi(obj_num1.get_numero(), obj_num2.get_numero())
            return self.resultado
        elif self.tipo_operacion == "Division":
            self.resultado = self.calcular_div(obj_num1.get_numero(), obj_num2.get_numero())
            return self.resultado
        else:
            return "ERROR: su tipo de operacion es invalida"
            pass

    def guardar_info(self,obj_usuario):
        self.texto_tabla = self.texto_tabla + f"cedula: {obj_usuario.get_cedula}"
        self.texto_tabla = self.texto_tabla + f"Numero: {obj_usuario.get_nombre}"
    

    def mostrar_tabla(self):
        print(self.texto_tabla)    


        
        

