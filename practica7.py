''' Dolores Fernanda Castillo De Dios '''

from ast import Expression
import re
from tkinter import _ExceptionReportingCallback
from unittest import result

carpeta_nombre="C:\\Users\\fer_c\OneDrive\Documentos\PLN\\Docs\\"

archivo_nombre="documento2.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
expresion_regular=re.compile(r"Procesamiento")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

''' -------------------------------- '''

expresion_regular=re.compile(r"Ni+")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado4 in resultados_busqueda:
    print(resultado4.group(0))