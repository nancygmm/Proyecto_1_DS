import pandas as pd
from pathlib import Path

def procesar_carpeta_completa(carpeta_xlsx, carpeta_csv=None, encoding='utf-8'):
    try:
        carpeta_xlsx = Path(carpeta_xlsx)
        
        if not carpeta_xlsx.exists():
            raise FileNotFoundError(f"La carpeta {carpeta_xlsx} no existe")
        
        if carpeta_csv is None:
            carpeta_csv = carpeta_xlsx
        else:
            carpeta_csv = Path(carpeta_csv)
            carpeta_csv.mkdir(exist_ok=True)
        
        archivos_xlsx = list(carpeta_xlsx.glob("*.xlsx"))
        
        if not archivos_xlsx:
            print("No se encontraron archivos XLSX en la carpeta")
            return []
        
        archivos_exitosos = []
        archivos_fallidos = []
        
        for i, archivo_xlsx in enumerate(archivos_xlsx, 1):
            try:
                print(f"\n[{i}/{len(archivos_xlsx)}] Procesando: {archivo_xlsx.name}")
                
                archivo_csv = carpeta_csv / f"{archivo_xlsx.stem}.csv"
                
                df = pd.read_excel(archivo_xlsx)
                df.to_csv(archivo_csv, index=False, encoding=encoding)
                
                print(f"   Convertido exitosamente")
                print(f"   {df.shape[0]} filas, {df.shape[1]} columnas")
                print(f"   Guardado como: {archivo_csv.name}")
                
                archivos_exitosos.append(str(archivo_csv))
                
            except Exception as e:
                print(f" Error: {str(e)}")
                archivos_fallidos.append(archivo_xlsx.name)
        
        
        return archivos_exitosos
        
    except Exception as e:
        print(f"Error general en el procesamiento: {str(e)}")
        return []


def main():
    
    carpeta_entrada = "departamentos"
    carpeta_salida = "departamentos_csv"
    
    procesar_carpeta_completa(carpeta_entrada, carpeta_salida)

if __name__ == "__main__":
    main()