import nltk
import matplotlib.pyplot as plt
from matplotlib import rcParams


carpeta_nombre="C:\\Users\\fer_c\\OneDrive\\Escritorio\\PLN\\docs\\"
archivo_nombre="UNIR.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")

tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)
print(palabras_totales)
print(palabras_diferentes)

texto_nltk=nltk.Text(tokens) 
distribucion=nltk.FreqDist(texto_nltk) 
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
hapaxes=distribucion.hapaxes()
print("\nPalabras que se encuentran 1 vez en el texto\n") 
for hapax in hapaxes: 
    print(hapax)

rcParams.update({"figure.autolayout":True})
distribucion.plot(cumulative=True)
distribucion.plot(20,cumulative=True)
