#Problema 1. Procesamiento de una lista de enteros. 
# Crea una función que reciba una lista de enteros por parámetro y devuelva otra 
# lista, de acuerdo a las siguientes acciones: 
# 1. Eliminar los números negativos de la lista. 
# 2. Eliminar los valores que están repetidos, quedándonos con uno de ellos. 
# 3. Ordenar los números resultantes de menor a mayor. 
# Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4]. 

def procesar_lista(numeros):
    """Elimina negativos y duplicados y ordena el resultado."""
    resultado = []

    for numero in numeros:
        if numero >= 0 and numero not in resultado:
            resultado.append(numero)

    resultado.sort()
    return resultado


# Pedir al usuario 8 números enteros
lista_original = []

while len(lista_original) < 8:
    try:
        numero = int(input(f"Introduce el número {len(lista_original) + 1} de 8: "))
        lista_original.append(numero)
    except ValueError:
        print("Entrada no válida. Introduce un número entero.")


# Procesar la lista y mostrar el resultado
lista_procesada = procesar_lista(lista_original)

print("Lista introducida:", lista_original)
print("Lista procesada:", lista_procesada)