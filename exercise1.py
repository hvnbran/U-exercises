""" 
Descripción
n1: Variable numerica de entrada real del primer número.
n2: Variable numerica de entrada real del segundo número.
numerofinal = Varible numerica real de proceso.
cuboo ó solucion: Varible numerica real de proceso y de salida que almacena el resultado. 
"""

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
numerofinal=(3* n1 ** 2 ) + (-5 * n2 **3)
cuboo = numerofinal ** 3
print("El resultado es:", cuboo)


"""
# | N1 | N2 | resultado                    | pantalla               |
# |-1  |-2  | (3*(-1**2)+(-5*(-2**3)))**3  | el resultado es 79507  |

Ingrese el primer numero: -1
Ingrese el segundo numero: -2
El resultado es: 79507
"""


