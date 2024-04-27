class Pizza():
    size = "familiar"
    price = 10000

    @staticmethod
    def validador (opciones, eleccion):
        return eleccion in opciones

    def orden_pedido(self):
        self.carne = int(input("Ingrese el ingrediente proteico: \n1)pollo \n2)vacuno \n3)carne vegetal\n"))
        self.vegetal_1 = int(input("Ingrese el ingrediente vegetal: \n1)tomate \n2)aceituna \n3)champiñones\n"))
        self.vegetal_2 = int(input("Ingrese el ingrediente vegetal: \n1)tomate \n2)aceituna \n3)champiñones\n"))
        self.masa = int(input("Ingrese el tipo de masa: \n1)Tradicional \n2)delgada\n"))
        
        op_carne = [1,2,3]
        op_vegetal = [1,2,3]
        op_masa = [1,2]

        valido = Pizza.validador(op_carne + op_vegetal + op_masa, [self.carne, self.vegetal_1, self.vegetal_2, self.masa])
        return valido
            






