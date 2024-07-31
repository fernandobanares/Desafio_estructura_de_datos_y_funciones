import sys

with open(sys.argv[1], "r") as file:
    texto=file.read()
    palabras = texto.split()
    palabras_distintas = set(palabras)
    num_palabras = len(palabras_distintas)
    print(f"El número de palabras distintas es:  {num_palabras}")
    cadena_palabras = ''.join(palabras_distintas)
    caracteres_distintos = set(cadena_palabras)
    num_caracteres_distintos = len(caracteres_distintos)
    print(f"El número de caracteres distintos es: {num_caracteres_distintos}")
       


