def operaciones_lista():
    lista = ["Camiseta", "Pantalón", "Zapatillas"]
    lista = lista + ["Abrigo"]
    lista = lista + ["Jersey", "Sudadera"]
    lista = lista + ["Calcetines"] + ["Bufanda"]
    return lista

lista_final = operaciones_lista()
print(lista_final) 