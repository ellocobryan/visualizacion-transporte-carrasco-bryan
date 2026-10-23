# Evaluación 2 - Visualización de Datos de Transporte

## Problema
Estudio exploratorio y análisis visual sobre el volumen, estacionalidad y comportamiento operacional de las aeronaves en Chile a partir de datos públicos de aviación civil.

## Fuente de datos
- **Institución:** Junta de Aeronáutica Civil (JAC) / Estado de Chile
- **Portal:** Datos.gob.cl
- **Dataset:** Operaciones de Aeronaves (Serie histórica ~11.16M de registros)

## Adquisición
Datos descargados directamente desde el portal oficial en formato Parquet y preservados intactos en `data/raw/bitacora-vuelos.parquet`.

## Configuración del entorno
Para reproducir el entorno de análisis ejecute en su terminal:

```bash
python -m venv .venv
# Activar entorno (Windows PowerShell)
.venv\Scripts\Activate.ps1
# O en Git Bash / Linux / Mac: source .venv/bin/activate
pip install -r requirements.txt
```

visualizacion-transporte-carrasco-bryan/
├── data/
│   ├── raw/               # Fuente original (bitacora-vuelos.parquet)
│   └── processed/         # Dataset procesado (transportes_procesado.parquet)
├── notebooks/
│   └── evaluacion02.ipynb # Notebook ejecutable secuencial
├── output/
│   └── figures/           # Visualizaciones exportadas (.png)
├── README.md              # Documentación técnica
├── requirements.txt       # Dependencias del proyecto
└── .gitignore             # Configuración de exclusiones Git

Perfilamiento
Registros evaluados: 11.163.791 filas

Columnas: 12 variables originales

Uso de Memoria RAM: ~2.53 GB

Comparación de Formatos: El formato Parquet demostró ser la alternativa óptima frente a CSV, reduciendo el almacenamiento en disco a 131.84 MB y acelerando los tiempos de lectura/escritura en Pandas.

Calidad de datos
Valores ausentes: Se detectaron nulos en numero_vuelo (4.32%) y pmd (2.46%).

Tratamiento: Los nulos en numero_vuelo se categorizaron como 'SIN_NUMERO' (asociados principalmente a operaciones no comerciales/privadas). La variable de peso máximo al despegue (pmd) fue convertida a tipo numérico continuo.

Preparación
Limpieza y normalización de cadenas de texto (mayúsculas y remoción de espacios) en campos de aerolíneas y aeropuertos. Generación de un archivo limpio sin modificar la fuente raw.

Variables derivadas
anio: Año de la operación derivado de la fecha dt_operacion.

mes: Mes del año (1-12) para evaluar estacionalidad.

trimestre: Agrupación trimestral (1-4) para análisis macro.

Dimensionalidad
Dimensiones: aerolinea_dgac (nominal), es_internacional (binaria/nominal), mes (ordinal/temporal), anio (temporal).

Medidas: operaciones (conteo discreto de vuelos), pmd (continuo).

Transformaciones analíticas
Aplicación de agrupaciones agregadas mediante groupby(), tablas pivote pivot_table() y ordenamiento sort_values() para estructurar matrices aptas para renderizado visual.

Diseño de visualizaciones
Se utilizaron principios de jerarquía visual, eliminación de elementos decorativos innecesarios (chartjunk) y mantenimiento de escalas proporcionales desde origen 0.

Matplotlib
Figura 01: Gráfico de barras horizontales para el Top 10 de aerolíneas con mayor volumen operacional.

Figura 02: Gráfico de líneas para mostrar la evolución histórica interanual de las operaciones.

Seaborn
Figura 03: Gráfico de conteo (countplot) con paleta viridis para analizar la distribución mensual del tráfico.

Figura 04: Matriz de calor (heatmap) para contrastar el comportamiento de vuelos nacionales versus internacionales.

Visualización multidimensional
Figura 05: Gráfico de dispersión (scatterplot) que integra 4 canales visuales:

Eje X: Mes del Año

Eje Y: Volumen de Operaciones

Color (Hue): Aerolínea Top

Tamaño (Size): Magnitud del flujo de operaciones

Benchmark visual
Figura 06: Comparación entre Gráfico de Líneas (Opción A - ideal para tendencia continua) vs. Gráfico de Barras (Opción B - ideal para comparar magnitudes discretas mensuales). Se concluye la superioridad de la Opción B para comunicar la estacionalidad intermensual clara.

Validación
Auditoría visual de gráficos para asegurar contraste adecuado, legibilidad de etiquetas en ejes y consistencia en los títulos.

Hallazgos
HALLAZGO 1 (Concentración): LAN / LATAM concentra la mayor cuota de mercado en el volumen de operaciones aéreas en Chile.

HALLAZGO 2 (Estacionalidad): Se observa un pico operacional pronunciado en los meses estivales (diciembre a marzo) y un descenso gradual hacia mediados de año (mayo-junio).

HALLAZGO 3 (Predominio Nacional): Los vuelos de carácter nacional superan de manera holgada a las operaciones internacionales en todos los meses evaluados.

Limitaciones
El dataset no incluye el detalle de retrasos o cancelaciones, por lo que el análisis se limita estrictamente a operaciones efectivamente registradas.

Consideraciones éticas
Se evitó la manipulación o truncamiento deliberado de ejes Y para no exagerar variaciones porcentuales de tráfico entre aerolíneas o periodos.

Conclusiones
El flujo de procesamiento desde datos brutos en Parquet hasta la construcción de gráficos multidimensionales permitió transformar más de 11 millones de registros en patrones visuales claros de estacionalidad y concentración de mercado.

Instrucciones de ejecución
Clonar el repositorio.

Descargar el dataset bitacora-vuelos.parquet desde Datos.gob.cl y colocarlo en data/raw/.

Ejecutar el notebook secuencial notebooks/evaluacion02.ipynb.

Autor
Bryan Carrasco