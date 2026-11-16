#Escribe una función que reciba por parámetro una lista de palabras y la ruta a 
# un fichero de texto y devuelva un diccionario que muestre cuantas veces 
# aparecen las distintas palabras de la lista en el fichero de texto. Haz un pequeño 
# programa que la ponga a prueba. 

import string

def contar_palabras(lista_palabras, ruta_fichero):
    frecuencias = {}

    for palabra in lista_palabras:
        frecuencias[palabra.lower()] = 0

    with open(ruta_fichero, "r", encoding="utf-8-sig") as fichero:
        texto = fichero.read().lower()

    print("CONTENIDO LEÍDO:", repr(texto))

    signos = string.punctuation + "¿¡«»“”‘’…—–"

    for signo in signos:
        texto = texto.replace(signo, " ")

    palabras_texto = texto.split()

    print("PALABRAS DETECTADAS:", repr(palabras_texto))

    for palabra in palabras_texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

    return frecuencias

# Programa de prueba
if __name__ == "__main__":
    palabras = []

    for i in range(5):
        palabra = input(f"Introduce la palabra {i + 1} de 5: ").strip().lower()

        while not palabra or len(palabra.split()) != 1 or palabra in palabras:
            if not palabra:
                print("No puedes dejar la palabra vacía.")
            elif len(palabra.split()) != 1:
                print("Introduce solo una palabra, sin espacios.")
            else:
                print("Esa palabra ya está en la lista. Introduce otra.")

            palabra = input(
                f"Introduce la palabra {i + 1} de 5: "
            ).strip().lower()

        palabras.append(palabra)

    ruta = r"C:\Users\Ospalus\PIA\PIA\texto.txt"

    resultado = contar_palabras(palabras, ruta)

    print("\nFrecuencia de las palabras:")

    for palabra in sorted(resultado):
        print(f"{palabra}: {resultado[palabra]}")