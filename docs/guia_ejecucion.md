# Guía de Replicabilidad del Proyecto

## Requisitos
- Python 3.10+
- Entorno virtual configurado (`.venv`)

## Pasos para ejecutar
1. Descargar `bitacora-vuelos.parquet` desde el portal Datos.gob.cl.
2. Colocar el archivo en `data/raw/`.
3. Activar el entorno virtual e instalar dependencias con `pip install -r requirements.txt`.
4. Abrir y ejecutar secuencialmente el notebook `notebooks/evaluacion02.ipynb`.