"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    df = pd.read_csv('clusters_report.txt', sep='|')
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['palabras clave'] = df['palabras clave'].str.replace(' ', ', ')
    return df
