#Ejemplo pandas
import pandas as pd

df = pd.read_csv("ejemplo.csv")
print(df.head())

for index, row in df.iterrows():
    print(row["Columna 1"], row["Columna 2"])

print(df.info())

df["Columna 1"] = df["Columna 1"] + 1
print(df.head())
print("\n\n\n")
df_prueba = pd.DataFrame({"Columna 1":[1,2,3,4,5], "Columna 2":["a","b","c","d","ej"]})
print(df_prueba.head())

df_prueba.to_csv("archivo_inventario.csv", index=False)
