from lib2to3.pgen2 import token
import nltk

carpeta_nombre=("C:\\Users\\fer_c\\OneDrive\\Escritorio\\PLN\\")
archivo_nombre="documento2.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
    print(token)

palabras_total=len(tokens)
print("palabras", palabras_total)

tokens_conjunto=set(tokens)
palabras_diferentes=len(tokens_conjunto)
print(palabras_diferentes)

riqueza_lexica=palabras_diferentes/palabras_total
print("riqueza lexica:",riqueza_lexica)
riqueza_lexicap=100*palabras_diferentes/palabras_total
print("riqueza lexica:", riqueza_lexicap,"%")

texto_nltk=nltk.Text(tokens)
texto_nltk.concordance("procesamiento")
texto_nltk.similar("procesamiento")

conteo_individual=tokens.count("procesamiento")
print("numero de veces qye se encuentra la palabra en el texto: ", conteo_individual)