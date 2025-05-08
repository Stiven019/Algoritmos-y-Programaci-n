datos = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}
valores = []
for valor in datos.values():
    if valor not in valores:
        valores.append(valor)
print(valores)