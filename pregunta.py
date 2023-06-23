"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    with open('clusters_report.txt') as archivo:
        filas = archivo.readlines()

    data = []
    row = []
    header = ['cluster', 'cantidad_de_palabras_clave', 
    'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    for fila in filas[4:]:
        if re.match('^ +\d+ +', fila):
            a = fila.split()
            row.append(int(a[0]))
            row.append(int(a[1]))
            row.append(float(a[2].replace(',','.')))
            row.append(' '.join(a[4:]))
        elif re.match('^ +\w', fila):
            a = fila.split()
            a = ' '.join(a)
            row[3] += ' ' + a
        elif re.match('^\n', fila) or re.match('^ +$', fila):
            row[3] = row[3].replace('.', '')
            data.append(row)
            row = []
    return pd.DataFrame (data, columns =header)
