''' Fernanda Castillo '''

carpeta_nombre="C:\\Users\\fer_c\OneDrive\Documentos\PLN"

archivo_nombre="doc2.txt"

with open(carpeta_nombre+archivo_nombre,"r")as archivo:
    texto=archivo.read()

    simbolos=["(",")",",",":",".",";","\""]
    for simbolo in simbolos:
        texto=texto.replace(simbolo," "+simbolo+" ")

        palabras_lista=texto.split()

        palabras_unicas=[] 

        for palabra in palabras_lista:
            if palabra in palabras_unicas:
                continue
            palabras_unicas.append(palabra)
    print(palabras_unicas)
    num=len(palabras_unicas)
    print("Numero de palabras en el documento: ",num)
    num2=len(palabras_lista)   
    print("Numero de palabras totales: ",num2)    

