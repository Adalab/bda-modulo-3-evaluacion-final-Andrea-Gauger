import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import warnings
warnings.filterwarnings("ignore")

from src import soporte_eda as sp1


df_activity = sp1.apertura_exploracion("Customer Flight Activity")
print("Explorando csv...")

df_history = sp1.apertura_exploracion("Customer Loyalty History")
print("Explorando csv...")

sp1.eliminar_duplicados(df_activity)
print("Eliminando duplicados...")

df_activity_limpio = sp1.eliminar_irrelevantes(df_activity, "Total Flights")
print("Eliminando filas con datos irrelevantes...")

sp1.union_cvs(df_activity_limpio, df_history)
print("Unión de dataframes y creación de nuevo csv")




