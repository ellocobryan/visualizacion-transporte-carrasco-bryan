import pandas as pd

def cargar_datos_procesados(filepath="../data/processed/transportes_procesado.parquet"):
    """Carga y retorna el dataset procesado de transporte."""
    return pd.read_parquet(filepath)