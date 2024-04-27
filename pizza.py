import ingredientes
#se crea la clase pizza
class Pizza():
    #se establecen los atributos
    size = "familiar"
    price = 10000

#se crea el metodo para validar las elecciones
    @staticmethod
    def validador (opciones, eleccion):
        return eleccion in opciones

#se crea el metodo para definir atributos de la pizza
    def orden_pedido(self):
        self.carne = 0
        self.vegetal_1 = 0
        self.vegetal_2 = 0
        self.masa = 0

        self.carne = int(input(f"Ingrese el ingrediente proteico: \n1){ingredientes.proteina[0]} \n2){ingredientes.proteina[1]} \n3){ingredientes.proteina[2]}\n"))
        if self.carne == 1:
            self.carne = ingredientes.proteina[0]
        elif self.carne == 2:
            self.carne = ingredientes.proteina[1]
        elif self.carne == 3:
            self.carne = ingredientes.proteina[2]
        self.vegetal_1 = int(input(f"Ingrese el ingrediente vegetal: \n1){ingredientes.vegetales[0]} \n2){ingredientes.vegetales[1]} \n3){ingredientes.vegetales[2]}\n"))
        if self.vegetal_1 == 1:
            self.vegetal_1 = ingredientes.vegetales[0]
        elif self.vegetal_1 == 2:
            self.vegetal_1 = ingredientes.vegetales[1]
        elif self.vegetal_1 ==3:
            self.vegetal_1 = ingredientes.vegetales[2]
        self.vegetal_2 = int(input(f"Ingrese el ingrediente vegetal: \n1){ingredientes.vegetales[0]} \n2){ingredientes.vegetales[1]} \n3){ingredientes.vegetales[2]}\n"))
        if self.vegetal_2 == 1:
            self.vegetal_2 = ingredientes.vegetales[0]
        elif self.vegetal_2 == 2:
            self.vegetal_2 = ingredientes.vegetales[1]
        elif self.vegetal_2 ==3:
            self.vegetal_2 = ingredientes.vegetales[2]
        self.masa = int(input(f"Ingrese el tipo de masa: \n1){ingredientes.tipo_masa[0]} \n2){ingredientes.tipo_masa[1]}\n"))
        if self.masa == 1:
            self.masa = ingredientes.tipo_masa[0]
        elif self.masa == 2: 
            self.masa = ingredientes.tipo_masa[1]

        p_final = [self.carne, self.vegetal_1, self.vegetal_2, self.masa]

        self.valido = Pizza.validador(ingredientes.proteina + ingredientes.vegetales + ingredientes.tipo_masa, p_final)
        return self.valido, self.carne, self.vegetal_1, self.vegetal_2, self.masa