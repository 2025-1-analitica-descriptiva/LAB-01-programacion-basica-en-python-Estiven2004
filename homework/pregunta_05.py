"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    max_min_por_letra = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                letra = parts[0]
                valor = int(parts[1])
                if letra in max_min_por_letra:
                    max_min_por_letra[letra][0] = max(max_min_por_letra[letra][0], valor)
                    max_min_por_letra[letra][1] = min(max_min_por_letra[letra][1], valor)
                else:
                    max_min_por_letra[letra] = [valor, valor]

    lista_ordenada = sorted([(letra, valores[0], valores[1]) for letra, valores in max_min_por_letra.items()])

    return lista_ordenada
