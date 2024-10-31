import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc, confusion_matrix
##########################################################################################################

df = pd.read_csv("Data/df_final.csv")
modelo = joblib.load("Data/Modelo_GradientBoosting.pkl")

def CurvaRoc():
    X = df[["fico_range_diff", "loan_income_ratio", "term_numeric", "interest_loan", 
             "loan_amnt", "annual_inc", "int_rate", "fico_range_high"]]
    y = df["pagado"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)

    y_pred_proba = modelo.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
    roc = auc(fpr, tpr)

    # para meter nuestro threshold
    threshold = 0.537
    threshold_index = np.argmax(thresholds >= threshold)
    threshold_fpr = fpr[threshold_index]
    threshold_tpr = tpr[threshold_index]

    curva_roc = px.area(
        x=fpr,
        y=tpr,
        title=f"Curva ROC (AUC = {roc:.2f})",
        labels=dict(x="Falsos Positivos",
                    y="Verdaderos Positivos"),
        line_shape="linear",
        color_discrete_sequence=["#6313ab"],
        width=700, height=500
    )
    
    curva_roc.add_shape(
        type="line", line=dict(dash="dash", color="#6313ab"),
        x0=0, x1=1, y0=0, y1=1
    )

    curva_roc.add_shape(
        type="line",
        x0=threshold_fpr,
        y0=threshold_tpr,
        x1=threshold_fpr,
        y1=0,  # Línea vertical hasta el eje X
        line=dict(color="red", width=2, dash="dash"),
    )

    st.plotly_chart(curva_roc)

##########################################################################################################

def ConfMatrix():
    X = df[["fico_range_diff", "loan_income_ratio", "term_numeric", "interest_loan", 
             "loan_amnt", "annual_inc", "int_rate", "fico_range_high"]]
    y = df["pagado"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)

    y_pred_proba = modelo.predict_proba(X_test)[:, 1]
# con esto aplicamos el threshold bueno de 0.537
    y_pred = (y_pred_proba >= 0.537).astype(int)

# visualizar
    conf_matrix = confusion_matrix(y_test, y_pred)
    fig_conf_matrix = px.imshow(conf_matrix, 
                                text_auto=True, 
                                labels=dict(x="Predicción", y="Verdadero"),
                                x=["No Pagado", "Pagado"], 
                                y=["No Pagado", "Pagado"],
                                color_continuous_scale="purples",
                                title="Matriz de Confusión")
    st.plotly_chart(fig_conf_matrix)

##########################################################################################################

def F_Importance():

    X = df[["fico_range_diff", "loan_income_ratio", "term_numeric", "interest_loan", 
             "loan_amnt", "annual_inc", "int_rate", "fico_range_high"]]  # Características
    y = df["loan_status"]  # Variable objetivo

    importances = modelo.feature_importances_
    feature_importances = pd.Series(importances, index=X.columns).sort_values(ascending=False)

    feature_importances_df = feature_importances.reset_index()
    feature_importances_df.columns = ["Características", "Importancia"]

    fig = px.bar(
        feature_importances_df,
        x="Importancia",
        y="Características",
        title="",
        labels={"Importancia": "Importancia", "Características": "Características"},
        color="Importancia",
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(
        xaxis_title="Importancia",
        yaxis_title="Características",
        plot_bgcolor='rgba(0,0,0,0)',
        template="plotly_white"
    )
    st.plotly_chart(fig)

##########################################################################################################
##########################################################################################################
# Análisis de variables seleccionadas y no seleccionadas
def AnalisisVar():
    
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; text-align: center;'>Análisis de Variables Seleccionadas y No Seleccionadas</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.write(""" 
    <strong style='color: violet; font-weight: bold;'>Variables Seleccionadas para el Modelo:</strong><br>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - <strong style='color: violet;'>fico_range_diff</strong>: La diferencia entre el puntaje FICO alto y bajo, que indica estabilidad crediticia del prestatario.
    - <strong style='color: violet;'>loan_income_ratio</strong>: Relación del monto del préstamo con el ingreso anual, reflejando la carga de deuda respecto a los ingresos.
    - <strong style='color: violet;'>term_numeric</strong>: Plazo en meses del préstamo, donde plazos más largos pueden implicar mayores riesgos.
    - <strong style='color: violet;'>interest_loan</strong>: Calculado como la tasa de interés por el monto del préstamo, aumentando el riesgo de pago para préstamos con altos intereses.
    - <strong style='color: violet;'>loan_amnt</strong>: Monto del préstamo solicitado, relevante porque préstamos de mayor cuantía pueden suponer mayor riesgo.
    - <strong style='color: violet;'>annual_inc</strong>: Ingreso anual del cliente, un predictor fuerte de capacidad de pago.
    - <strong style='color: violet;'>int_rate</strong>: Tasa de interés del préstamo; tasas más altas suelen indicar un perfil de mayor riesgo.
    - <strong style='color: violet;'>fico_range_high</strong>: Puntaje FICO alto dentro del rango del cliente, indicando mejor perfil crediticio.
    """, unsafe_allow_html=True)

    st.write("""
    <strong style='color: violet; font-weight: bold;'>Variables No Seleccionadas:</strong><br>
    """, unsafe_allow_html=True)

    st.markdown("""
    - <strong style='color: violet;'>Saldo Pendiente (out_prncp)</strong>: Refleja el progreso del pago del préstamo, más que el riesgo inicial de crédito del cliente.
    - <strong style='color: violet;'>Recuperaciones por Impago (recoveries)</strong>: Indicador de fondos recuperados tras impago, útil en la recuperación de deudas más que en la predicción inicial.
    - <strong style='color: violet;'>Total Principal Devuelto (total_rec_prncp)</strong>: Muestra cuánto del principal ha sido devuelto, indicador útil para préstamos ya en curso.

    **Estas variables no seleccionadas representan aspectos de préstamos que ya han sido concedidos, mientras que el modelo se enfoca en el análisis de viabilidad inicial de un préstamo**.
    """, unsafe_allow_html=True)

##########################################################################################################
# Explicacion de las visualizaciones de matriz de confusion y curva roc
def RocConf():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; text-align: center;'>Visualización del Modelo mediante Matriz de Confusión y Curva ROC</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("""
    <p class="big-font">
    La <strong style='color: violet; font-weight: bold;'>matriz de confusión</strong> es una herramienta que permite evaluar el desempeño de un modelo de clasificación. Muestra la relación entre las predicciones y los valores reales, facilitando la identificación de errores en las clasificaciones.
    </p>
    <p class="big-font">
    La <strong style='color: violet; font-weight: bold;'>curva ROC</strong> (Receiver Operating Characteristic) es una representación gráfica que muestra el rendimiento de un modelo de clasificación a diferentes umbrales de decisión. Permite visualizar la tasa de verdaderos positivos frente a la tasa de falsos positivos, y el área bajo la curva (AUC) indica la capacidad del modelo para distinguir entre clases.
    </p>
    <p class="big-font"> 
    <strong style='color: violet; font-weight: bold;'>A continuación, puedes seleccionar la visualización que desees analizar</strong>:
    </p>
    """, unsafe_allow_html=True)

    visual = st.radio("Selecciona el tipo de visualización:", ("Matriz de Confusión", "Curva ROC"))
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    if visual == "Matriz de Confusión":
        with col1:
            st.header("Explicación de la Matriz de Confusión:")
            st.markdown("""
            <p class="big-font">
            La <strong style='color: violet; font-weight: bold;'>matriz de confusión</strong> presenta un resumen de los <strong style='color: violet; font-weight: bold;'>aciertos</strong> y <strong style='color: violet; font-weight: bold;'>errores</strong> del <strong style='color: violet; font-weight: bold;'>modelo</strong>, dividiéndolos en cuatro categorías:
            </p>
            <ul>
                <li><strong style='color: violet; font-weight: bold;'>Verdaderos Positivos (TP):</strong> Predicciones correctas de un <strong style='color: violet; font-weight: bold;'>resultado positivo</strong>.</li>
                <li><strong style='color: violet; font-weight: bold;'>Verdaderos Negativos (TN):</strong> Predicciones correctas de un <strong style='color: violet; font-weight: bold;'>resultado negativo</strong>.</li>
                <li><strong style='color: violet; font-weight: bold;'>Falsos Positivos (FP):</strong> Predicciones incorrectas de los <strong style='color: violet; font-weight: bold;'>resultados positivos</strong>.</li>
                <li><strong style='color: violet; font-weight: bold;'>Falsos Negativos (FN):</strong> Predicciones incorrectas de los <strong style='color: violet; font-weight: bold;'>resultados negativos</strong>.</li>
            </ul>
            <p class="big-font">
            Esto permite calcular métricas como <strong style='color: violet; font-weight: bold;'><u title="Proporción de verdaderos positivos entre todos los casos positivos predichos.">precisión</u></strong>, 
            <strong style='color: violet; font-weight: bold;'><u title="Proporción de verdaderos positivos entre todos los casos positivos reales.">recall</u></strong> y 
            <strong style='color: violet; font-weight: bold;'><u title="Media armónica entre precisión y recall, proporciona un balance entre ambas métricas.">F1-score</u></strong>, que son fundamentales para entender el <strong style='color: violet; font-weight: bold;'>desempeño del modelo</strong>.
            </p>
            <p class="big-font">
            En nuestra matriz de confusión, observamos <strong style='color: violet; font-weight: bold;'>5130 verdaderos no pagados</strong> y <strong style='color: violet; font-weight: bold;'>3781 verdaderos pagados</strong>, lo que indica que el modelo ha clasificado correctamente una gran parte de los casos. Sin embargo, también tenemos <strong style='color: violet; font-weight: bold;'>1268 falsos pagados</strong> y <strong style='color: violet; font-weight: bold;'>1951 falsos no pagados</strong>, lo que nos da una oportunidad para mejorar el modelo. A pesar de estos errores, los resultados sugieren que el modelo tiene un desempeño <strong style='color: violet; font-weight: bold;'>sólido y prometedor</strong>.
            </p>
            """, unsafe_allow_html=True)

        with col2:
            ConfMatrix()

    else:
        with col1:
            st.header("Explicación de la Curva ROC:")
            st.markdown("""
            <p class="big-font">
            La  <strong style='color: violet; font-weight: bold;'>Curva ROC</strong> ilustra el rendimiento</strong> del modelo a medida que  <strong style='color: violet; font-weight: bold;'>varían los umbrales</strong> de clasificación. Un  <strong style='color: violet; font-weight: bold;'>modelo perfecto</strong> tendrá una curva que pasa por el punto  <strong style='color: violet; font-weight: bold;'>(0, 1)</strong>, lo que significa que tiene una tasa de  <strong style='color: violet; font-weight: bold;'>verdaderos positivos</strong> del  <strong style='color: violet; font-weight: bold;'>100%</strong> y una tasa de  <strong style='color: violet; font-weight: bold;'>falsos positivos</strong> del  <strong style='color: violet; font-weight: bold;'>0%</strong>.
            </p>
            <p class="big-font">
            El <strong style='color: violet; font-weight: bold;'>área bajo la curva (AUC)</strong> proporciona una medida única de la capacidad del modelo para <strong style='color: violet; font-weight: bold;'>clasificar correctamente</strong>. Un <strong style='color: violet; font-weight: bold;'>AUC de 1.0</strong> indica un <strong style='color: violet; font-weight: bold;'>modelo perfecto</strong>, mientras que un <strong style='color: violet; font-weight: bold;'>AUC de 0.5</strong> indica un modelo que <strong style='color: violet; font-weight: bold;'>no es mejor que el azar</strong>.
            </p>
            <p class="big-font">
            Un <strong style='color: violet; font-weight: bold;'>área bajo la curva (AUC) de 0.81</strong>, como en este caso, indica que nuestro modelo tiene una <strong style='color: violet; font-weight: bold;'>buena capacidad</strong> para <strong style='color: violet; font-weight: bold;'>clasificar correctamente</strong> los resultados. Este valor sugiere que el modelo es capaz de distinguir entre las clases positiva y negativa con un <strong style='color: violet; font-weight: bold;'>82% de precisión</strong> en promedio. 
            Aunque no es un modelo perfecto, un <strong style='color: violet; font-weight: bold;'>AUC de 0.81</strong> es un indicativo de un <strong style='color: violet; font-weight: bold;'>desempeño sólido</strong>, donde el modelo <strong style='color: violet; font-weight: bold;'>supera significativamente</strong> la <strong style='color: violet; font-weight: bold;'>clasificación aleatoria</strong>, que tendría un <strong style='color: violet; font-weight: bold;'>AUC de 0.5</strong>.
            </p>
            """, unsafe_allow_html=True)

        with col2:
            CurvaRoc()

##########################################################################################################

def Desc_FImportance():

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; text-align: center;'>Feature Importance</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("""
    <p class="big-font">
    La <strong style='color: violet; font-weight: bold;'>importancia de las características</strong> o <strong style='color: violet; font-weight: bold;'>feature importance </strong>es una medida que indica <strong style='color: violet; font-weight: bold;'>qué tan relevantes</strong> son las diferentes variables en un <strong style='color: violet; font-weight: bold;'>modelo de predicción</strong> para influir en la <strong style='color: violet; font-weight: bold;'>variable objetivo</strong>. Al conocer la importancia de cada característica, podemos entender cuáles variables tienen <strong style='color: violet; font-weight: bold;'>más peso</strong> en las decisiones del modelo.
    </p>
    <p class="big-font">
    Este análisis no solo ayuda a <strong style='color: violet; font-weight: bold;'>mejorar la interpretación</strong> del modelo, sino que también permite <strong style='color: violet; font-weight: bold;'>optimizarlo</strong> al centrarse en las características más relevantes, eliminando las que no aportan valor. Esto puede resultar en un modelo <strong style='color: violet; font-weight: bold;'>más simple</strong>, <strong style='color: violet; font-weight: bold;'>eficiente</strong> y con <strong style='color: violet; font-weight: bold;'>mejor capacidad</strong> de generalización.
    </p>
    <p class="big-font">
    A continuación, puedes ver, de forma visual, la importancia de las características, lo que nos proporciona información valiosa sobre cómo cada variable impacta en las predicciones.
    </p>
    """, unsafe_allow_html=True)
