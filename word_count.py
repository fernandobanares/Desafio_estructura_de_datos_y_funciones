with open("texto.txt", "r") as file:
    texto=file.read()

palabras = texto.count(lorem_ipsum.txt)

print(f"El texto tiene {palabras} palabras")

