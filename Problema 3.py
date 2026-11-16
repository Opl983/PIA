#Problema 3. Trabajo con conjuntos
# Escribe una función que reciba dos listas de enteros y devuelva un diccionario 
# con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA 
# CALCULARLOS) 
# 1. La intersección de ambos conjuntos (elementos comunes). 
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados). 
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto, 
# pero no en ambos).

def operaciones_conjuntos(lista1, lista2):
    # Convertimos las listas en conjuntos.
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Calculamos las operaciones utilizando conjuntos.
    resultado = {
        "interseccion": conjunto1 & conjunto2,
        "union": conjunto1 | conjunto2,
        "diferencia_simetrica": conjunto1 ^ conjunto2
    }

    return resultado


def pedir_lista(mensaje):
    while True:
        entrada = input(mensaje)

        try:
            lista = [int(numero) for numero in entrada.split()]
            return lista
        except ValueError:
            print("Entrada incorrecta. Introduce solo enteros separados por espacios.")


# Programa de prueba
if __name__ == "__main__":
    lista1 = pedir_lista(
        "Introduce los enteros de la primera lista separados por espacios: "
    )

    lista2 = pedir_lista(
        "Introduce los enteros de la segunda lista separados por espacios: "
    )

    resultado = operaciones_conjuntos(lista1, lista2)

    print("\nPrimera lista:", lista1)
    print("Segunda lista:", lista2)

    print("\nResultados:")
    print("Intersección:", sorted(resultado["interseccion"]))
    print("Unión:", sorted(resultado["union"]))
    print(
        "Diferencia simétrica:",
        sorted(resultado["diferencia_simetrica"])
    )