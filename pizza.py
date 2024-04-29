from ingredientes import Ingredientes

#se crea la clase pizza
class Pizza():
    #se establecen los atributos
    size = "familiar"
    price = 10000

#se crea el metodo para validar las elecciones
    @staticmethod
    def validador (opciones, eleccion):
        return all(ingrediente in opciones for ingrediente in eleccion)

#se crea el metodo para definir atributos de la pizza
    def orden_pedido(self):
        self.carne = 0
        self.vegetal_1 = 0
        self.vegetal_2 = 0
        self.masa = 0

        self.carne = int(input(f"Ingrese el ingrediente proteico: \n1){Ingredientes.proteina[0]} \n2){Ingredientes.proteina[1]} \n3){Ingredientes.proteina[2]}\n"))
        if self.carne == 1:
            self.carne = Ingredientes.proteina[0]
        elif self.carne == 2:
            self.carne = Ingredientes.proteina[1]
        elif self.carne == 3:
            self.carne = Ingredientes.proteina[2]
        self.vegetal_1 = int(input(f"Ingrese el ingrediente vegetal: \n1){Ingredientes.vegetales[0]} \n2){Ingredientes.vegetales[1]} \n3){Ingredientes.vegetales[2]}\n"))
        if self.vegetal_1 == 1:
            self.vegetal_1 = Ingredientes.vegetales[0]
        elif self.vegetal_1 == 2:
            self.vegetal_1 = Ingredientes.vegetales[1]
        elif self.vegetal_1 ==3:
            self.vegetal_1 = Ingredientes.vegetales[2]
        self.vegetal_2 = int(input(f"Ingrese el ingrediente vegetal: \n1){Ingredientes.vegetales[0]} \n2){Ingredientes.vegetales[1]} \n3){Ingredientes.vegetales[2]}\n"))
        if self.vegetal_2 == 1:
            self.vegetal_2 = Ingredientes.vegetales[0]
        elif self.vegetal_2 == 2:
            self.vegetal_2 = Ingredientes.vegetales[1]
        elif self.vegetal_2 ==3:
            self.vegetal_2 = Ingredientes.vegetales[2]
        self.masa = int(input(f"Ingrese el tipo de masa: \n1){Ingredientes.tipo_masa[0]} \n2){Ingredientes.tipo_masa[1]}\n"))
        if self.masa == 1:
            self.masa = Ingredientes.tipo_masa[0]
        elif self.masa == 2: 
            self.masa = Ingredientes.tipo_masa[1]

        p_final = [self.carne, self.vegetal_1, self.vegetal_2, self.masa]

        self.valido = Pizza.validador(Ingredientes.proteina + Ingredientes.vegetales + Ingredientes.tipo_masa, p_final)
        return self.valido, self.carne, self.vegetal_1, self.vegetal_2, self.masa