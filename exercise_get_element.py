# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    if len(lista)< indice or indice < -len(lista):
        return None
    elif len(lista)==0:
        return None
    
    else:
        return lista[indice]


