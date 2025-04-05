import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings("ignore")


def apertura_exploracion(csv):

    """ Función para leer csv, convertir a df y hacer una primera exploración.
    Igualar a variable con el nombre que quieres dar a DataFrame"""
    
    try:
        # Convertir el csv a DataFrame
        df = pd.read_csv(f"files/{csv}.csv")        

        # Muestro las primeras filas
        df.head()

        # Obtengo las listas
        print(f"-----\n\nEl DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n-----")

        # Consulto si hay filas duplicadas
        print(f"\nEl número de filas duplicadas es {df.duplicated().sum()}\n-----")

        # Muestro el tipo de dato y si hay nulos por cada columna
        print("\nInformación del DataFrame:")
        df.info()

        # Muestro las estadísticas de columnas numéricas
        print("-----\n\nEstadísticas descriptivas:")
        df.describe().T

        # Me devuelve un df que tendré que igualar a una variable
        return df  
                

    # Excepciones en caso de no encontrar el archivo o de que haya un error
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '../files/{csv}.csv'.")
        return None  
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None 
    

def eliminar_duplicados(df):
    """ Función para eliminar duplicados"""

    print(f"El df tiene {df.shape[0]} filas y {df.shape[0]} columnas.")
    print(f"Duplicados en df: {df.duplicated().sum()}")

    df = df.drop_duplicates()
    print("Eliminando filas duplicadas")

    print(f"Comprobamos que los duplicados se hayan eliminado. \nDuplicados en df: {df.duplicated().sum()}")

    return(f"El df tiene {df.shape[0]} filas y {df.shape[0]} columnas.")


def eliminar_irrelevantes(df, columna):
    """ Función para eliminar filas con datos irrelevantes"""
    print(f"El df tiene {df.shape[0]} filas y {df.shape[1]} columnas.")
    print(f"El df contiene {df[df[columna] > 0].shape[0]} filas y {df[df[columna] > 0].shape[1]} columnas con datos relevantes en la variable {columna}.")
    
    df = df[df[columna] > 0]
    print("Eliminando filas irrelevantes")
    print(f"El df tiene {df.shape[0]} filas y {df.shape[1]} columnas.")
    
    return df


def union_cvs(df1, df2):
    """ Función para unir ambos df y guardar en un nuevo csv.
    Igualar a una variable"""

    df3 = pd.merge(df1, df2, on="Loyalty Number", how="left")
    print("Uniendo los df")

    print(f"El nuevo df tiene {df3.shape[0]} filas y {df3.shape[1]} columnas.")

    df3.to_csv("files/Full Loyalty Program.csv", index=False)
    print("Guardando archivo como Full Loyalty Program.csv ")

