
# Creamos un archivo llamado 'my_notes.txt' y escribimos tres líneas de notas personales

with open("my_notes.txt", "w") as file:
    file.write("Hoy fue un dia muy lluvioso.\n")
    file.write("Me gusta aprender a programar en python.\n")
    file.write("Todos los dias es bueno para aprender.\n")

# Abrimos el archivo y leemos su contenido línea por línea, mostrando cada una en consola

with open("my_notes.txt", "r") as file:
    for linea in file:
        print(linea.strip())  # .strip() elimina el salto de línea al final