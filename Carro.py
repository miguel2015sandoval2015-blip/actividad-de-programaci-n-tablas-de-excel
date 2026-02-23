class carro: 
    def __init__(self,carro):
        self.carro = carro 

    def get_carro(self):
        return self.carro

    def set_carro(self,nuevo_carro):
        self.carro = nuevo_carro

    def imprimir_info(self):
        print(f"la placa del carro es : {self.carro}")            
    