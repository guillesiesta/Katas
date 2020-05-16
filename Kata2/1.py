precio = 3.49
descuento = 1.0 - 0.6
precio_con_descuento = precio * descuento

numero_de_barras = input("Dime cuantas putas barras de pan quieres o te reviento: ")
numero_de_barras = float(numero_de_barras)

print("Precio habitual para gays: "+str(precio))
print("Descuento: " + str(precio_con_descuento))
print("Coste final: "+ str(precio_con_descuento*numero_de_barras))