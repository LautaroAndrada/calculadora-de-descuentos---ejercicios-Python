#Consigna: Imagina que vas a comprar unas zapatillas que cuestan $45000 y tienen un descuento del 18%

precio = float(input("Ingrese el precio: "))

descuento = 18

totalDescuento = (precio*(descuento/100))
precioFinal = precio-totalDescuento

print(f"El resultado final es, el precio original fue de {precio} con un descuento del {descuento}%")
print(f"El descuento a aplicar queda en {totalDescuento} quedando el precio final en {precioFinal}")
