"""

En una pasteleria, el administrador realiza una promocion por la venta de sus buñuelos y sus pasteles
Por la venta de 7 buñuelos cobra 2000$
Por la venta de 5 pasteles cobra 5000$
Calcule el valor a pagar por una venta
--------------------------------------
Muestre(cuantos buñuelos...)
lea cantidad_buñuelos
costo_buñuelo = 2000 div 7
Lea costo_buñuelo

venta = cantidad_buñuelos * costo_buñuelo
lea venta
imprima = su precio es: int venta

Muestre(cuantos pasteles...)
lea cantidad_pasteles
costo_pastel = 5000 div 5
Lea costo_pastel

venta2 = cantidad_pasteles * costo_pastel
lea venta2
imprima = su precio es: int venta
--------------------------------------
Prueba de escritorio

Buñuelos  | pasteles  | Resultado1          | Resultado2           | Pantalla 1  | Pantalla 2
   1      |     2     |     2000/7 * 1      | 5000/5 * 2           |   285       |  2000

"""

cantidad_buñuelos = int(input("¿Cuantos buñuelos quiere comprar?: "))
costo_buñuelo = 2000/7

venta= cantidad_buñuelos * costo_buñuelo

print ("Su precio es: $", int(venta))

cantidad_pasteles = int(input("¿Cuantos pasteles quiere comprar?: "))
costo_pastel = 5000/5

venta2= cantidad_pasteles * costo_pastel
print ("Su precio es: $", int(venta2))


"""
¿Cuantos buñuelos quiere comprar?: 1
Su precio es: $ 285
¿Cuantos pasteles quiere comprar?: 2
Su precio es: $ 2000
"""
