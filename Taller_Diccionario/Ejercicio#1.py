lista_1=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
diccionario={}
for i in lista_1:
    diccionario.update({i:lista_1.count(i)})
print(diccionario)