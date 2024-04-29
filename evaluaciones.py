#se importan las librerias a utilizar
from pizza import Pizza
import ingredientes

#requerimiento 5.a
print(Pizza.size, Pizza.price)

#requerimiento 5.b
print(Pizza.validador(["salsa de tomate", "salsa bbq"], ["salsa de tomate"]))

#requerimiento 5.c
p_eva = Pizza()
p_eva.orden_pedido()

print(p_eva.carne)
print(p_eva.vegetal_1)
print(p_eva.vegetal_2)
print(p_eva.masa)
print(p_eva.valido)
print(Pizza.valido)
