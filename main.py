def calcular_costo_entrada(edad):
    if edad <= 14 or edad >= 65:
        costo_entrada = 5000
    else:
        costo_entrada = 15000
    return costo_entrada

def main():
    edad = int(input("Ingrese la edad de la persona: "))
    costo_entrada = calcular_costo_entrada(edad)
    print("El costo de entrada es:", costo_entrada)

if __name__ == "__main__":
    main()
    
""" Inicio
    Solicitar la edad de la persona
    Si la edad es menor o igual a 14 o mayor o igual a 65 entonces
        Asignar el costo de entrada a $5000
    De lo contrario
        Asignar el costo de entrada a $15000
    Mostrar el costo de entrada
Fin
"""