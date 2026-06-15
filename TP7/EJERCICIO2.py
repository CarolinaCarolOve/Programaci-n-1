linea = " mara ; programacion ; ocho "

partes = linea.split(";")
nombre = partes[0].strip().capitalize()
materia = partes[1].strip().capitalize()
nota_texto = partes[2].strip()

if nota_texto.isnumeric():
    nota = int(nota_texto)
    print(f"{nombre} cursa {materia} y obtuvo {nota}")
else:
    print("La nota no es valida")