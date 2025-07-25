# Proyecto 1 - Obtención y Limpieza de Datos

Este proyecto corresponde al curso de **Minería de Datos** y tiene como objetivo realizar un análisis y limpieza inicial de un conjunto de archivos `.csv` que contienen información de establecimientos educativos por departamento.

---

## Integrantes del grupo

* Gabriela Mazariegos - 22513
* Giovanni Santos - 22523
* Santiago Pereira - 22318
* Brandon Reyes - 22992

---

## Estructura del proyecto

```
Proyecto_1_DS/
│
├── departamentos_csv/               # Carpeta con los archivos .csv de cada departamento
│   ├── alta_verapaz.csv
│   ├── baja_verapaz.csv
│   └── ... (22 archivos en total)
│
├── analisis.ipynb                   # Jupyter Notebook con el análisis y estrategias de limpieza
├── estadisticas.txt                # Archivo con estadísticas generales (filas, columnas, duplicados)
├── conversor.py                    # Script adicional para pruebas o lectura
├── README.md                       # Este archivo
```

---

## Avances del proyecto 1

### 1. Descripción del conjunto de datos

- Total de archivos CSV: 22 (uno por departamento).
- Total de filas combinadas: **18,586**
- Total de columnas: **17**
- Cada archivo contiene información de establecimientos como nombre, dirección, municipio, director, supervisor, entre otros.

### 2. Variables con más necesidad de limpieza

- `ESTABLECIMIENTO`
- `DIRECCION`
- `TELEFONO`
- `SUPERVISOR`
- `DIRECTOR`
- `MUNICIPIO`
- `AREA`

### 3. Estrategia de limpieza general

- Unificación de mayúsculas/minúsculas
- Eliminación de caracteres especiales innecesarios
- Corrección ortográfica de nombres y direcciones
- Estandarización de formatos (ej. teléfonos, nombres)
- Validación contra listas oficiales (municipios)
- Eliminación de duplicados y columnas irrelevantes (`Unnamed: 0`)

### 4. Ejemplo aplicado: variable `ESTABLECIMIENTO`

- Se aplicarán funciones para:
  - Pasar a minúsculas
  - Eliminar espacios y caracteres extra
  - Unificar nombres escritos de formas diferentes
  - Eliminar duplicados exactos

---

## Estadísticas clave

- El dataset crudo presenta:
  - Variables con escritura inconsistente
  - Valores nulos en columnas clave como `TELEFONO`
  - Duplicados por diferencias mínimas de ortografía
  - Alta cardinalidad en nombres y supervisores

---

## Notas finales

Este proyecto será la base para aplicar técnicas de preprocesamiento, normalización y modelado posterior. Se continuará trabajando en la limpieza efectiva y validación de las transformaciones.

---

 *Última actualización: Julio 2025*
