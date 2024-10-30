import pandas as pd
import os

# Cargar el archivo CSV
file_path = 'C:/Users/luisc/OneDrive/Escritorio/BDA/sales_data.csv'

# Leer el archivo y cargarlo en un DataFrame de pandas
try:
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    print("Archivo cargado exitosamente en memoria.")

    # Eliminar las filas donde el valor de la columna 'state' esté vacío o sea null
    data_cleaned = data.dropna(subset=['STATE'])

    # Crear la carpeta de salida si no existe
    output_folder = 'C:/Users/luisc/OneDrive/Escritorio/BDA/Laboratorio6'
    os.makedirs(output_folder, exist_ok=True)
    
    # Guardar el DataFrame limpio en un archivo XML en la carpeta de salida
    output_path = os.path.join(output_folder, 'cleaned_data.xml')
    data_cleaned.to_xml(output_path, index=False)
    
    print(f"Datos guardados exitosamente en el archivo XML: {output_path}")

except FileNotFoundError:
    print("Archivo no encontrado. Por favor verifica la ruta.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
