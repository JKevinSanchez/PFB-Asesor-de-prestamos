# Asesor de Préstamos con Ciencia de Datos

## Descripción

Este proyecto tiene como objetivo construir un modelo de machine learning que ayude a evaluar la viabilidad de otorgar préstamos a los solicitantes en función de su perfil financiero. Utilizando algoritmos de clasificación y técnicas de análisis de datos, el modelo puede predecir la probabilidad de que un solicitante cumpla con los pagos del préstamo, proporcionando recomendaciones para los analistas financieros y gestores de riesgos.

## Objetivo

El objetivo principal de este proyecto es mejorar el proceso de toma de decisiones para la aprobación de préstamos, minimizando el riesgo de impago y aumentando la rentabilidad de la entidad crediticia.

## Estructura del Proyecto

- **data/**: Contiene los conjuntos de datos utilizados para entrenar y probar el modelo.
- **notebooks/**: Incluye notebooks de Jupyter que documentan el proceso de análisis y modelado.
- **scripts/**: Scripts de Python que implementan la preparación de datos, el entrenamiento del modelo y las pruebas.
- **models/**: Carpeta donde se almacenan los modelos entrenados y sus métricas de rendimiento.
- **results/**: Contiene los reportes y gráficos generados durante el análisis.
- **README.md**: Documento de introducción y guía del proyecto (este archivo).

## Requisitos

- Python 3.8 o superior
- Jupyter Notebook
- Librerías:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
  - joblib (para guardar y cargar modelos)
  - streamlit (creación de aplicación)

## Descripción del proceso

1. **Recolección de datos**: https://www.kaggle.com/datasets/wordsforthewise/lending-club
2. **Preprocesamiento de datos**: Se realiza limpieza de datos, manejo de valores faltantes y codificación de variables categóricas.
3. **Exploración de datos**: Análisis de tendencias y patrones en los datos para identificar caracterñisticas relevantes.
4. **Ingeniería de características**: Creación y selección de características que mejoran el rendimiento del modelo.
5. **Entrenamiento del modelo**: Se prueban diferentes algoritmos (e.g, árboles de decisión, regresión logística, random forest) para seleccionar el modelo más adecuado.
6. **Evaluación**: Validación del modelo con métricas como precisión, sensibilidad y matriz de confusión.
7. **Despliegue**: Implementación del modelo en un aplicación que permite ingresar datos de un solicitante y obtener una recomendación de préstamo.

## Resultados

El modelo alcanza una precisión del **0,537**, lo que permite a los asesores de préstamos tomar decisiones informadas. La recomendación final incluye detalles sobre el nivel de riesgo y el monto sugerido del préstamo.
