''' Fernanda Castillo '''

carpeta_nombre="C:\\Users\\fer_c\\OneDrive\\Documentos\\PLN"

archivo_nombre="doc3.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_listas=archivo.readlines()

palabra=input("Escribe la palabra a buscar en el archivo: ")

num_palabras=0
num_lineas=1
num_texto=0
num_vacio=0

for linea in lineas_listas:
    if linea.strip()==" ":
        num_lineas=num_lineas+1
        print("LINEA",num_lineas,":","Esta linea esta vacia")
        num_vacio=num_vacio+1

    else:
        num_lineas=num_lineas+1
        print("LINEA",num_lineas,":",linea)
        num_texto=num_texto+1
        if palabra in linea:
            num_palabras=num_palabras+1
print("Lineas totales: ",num_lineas)
print("Lineas con texto: ",num_texto)            
print("Lineas vacias: ",num_vacio)            
print("La palabra: ",palabra,"se encuentra",num_palabras,"veces en el documento.")            

