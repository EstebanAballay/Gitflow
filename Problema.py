class Producto:
    def init(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def  calcularIVA(precio):
        print("Calculando IVA para", precio)
        return precio * 1.21