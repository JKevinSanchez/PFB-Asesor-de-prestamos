import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from sklearn.metrics import roc_curve, auc, confusion_matrix
from sklearn.model_selection import train_test_split

def Metodologia():

    st.subheader("Metodología, Resultados y Conclusiones")
    
    # Explicación de la metodología Scrum
    st.write("""
    ### Metodología
    Para organizar el trabajo de este proyecto, utilizamos una metodología ágil llamada **Scrum**. 
    Scrum es un enfoque que permite dividir el proyecto en tareas más pequeñas y manejables, denominadas *sprints*. 
    Cada sprint tiene una duración fija (en este caso, dos semanas), y al final de cada sprint, evaluamos el progreso 
    y hacemos ajustes según sea necesario. Esto nos ayuda a adaptarnos a los cambios de forma rápida y a mejorar 
    continuamente, asegurándonos de que el proyecto evoluciona en la dirección correcta a medida que recibimos comentarios y nuevos conocimientos.
    """)
    
    # Carga y preparación de datos
    df_final = pd.read_csv("Data/df_final.csv")
    best_gb_model = joblib.load("Data/Modelo_GradientBoosting.pkl")

    st.markdown("---")
    
    st.write("""
    ### Modelo de Predicción Utilizado: Gradient Boosting
    Para predecir si un préstamo es viable o no, elegimos un modelo de *aprendizaje automático* llamado 
    **Gradient Boosting Classifier**. Este modelo funciona como una serie de "árboles de decisión". 
    Imaginemos estos árboles como secuencias de preguntas que el modelo responde para entender mejor los datos. 
    Por ejemplo, puede preguntarse: "¿El ingreso anual es mayor a cierto umbral?", o "¿El cliente tiene menos de un 30% de su crédito utilizado?". 
    Cada árbol intenta mejorar lo que el anterior no pudo predecir bien, como si fueran entrenadores de un equipo trabajando juntos para ayudar a tomar mejores decisiones.
    
    #### ¿Por qué Gradient Boosting es Útil?
    El modelo aprende de sus errores. Cada vez que un árbol no acierta, el siguiente árbol se enfoca en esas áreas problemáticas, logrando un modelo 
    que puede hacer predicciones más exactas. Esto es especialmente útil cuando queremos separar clientes en aquellos que probablemente paguen y 
    aquellos que tienen un mayor riesgo de no pagar.
    """)

    # División de los datos
    X = df_final[["fico_range_diff", "loan_income_ratio", "term_numeric", "interest_loan", 
                  "loan_amnt", "annual_inc", "int_rate", "fico_range_high"]]
    y = df_final["pagado"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    y_pred_proba = best_gb_model.predict_proba(X_test)[:, 1]
    y_pred = best_gb_model.predict(X_test)

    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    fig_roc = px.area(
        x=fpr, y=tpr,
        title=f"Curva ROC (AUC = {roc_auc:.2f})",
        labels=dict(x="Falsos Positivos", y="Verdaderos Positivos"),
        width=700, height=500
    )
    fig_roc.add_shape(
        type="line", line=dict(dash="dash"),
        x0=0, x1=1, y0=0, y1=1
    )
    st.plotly_chart(fig_roc)

    conf_matrix = confusion_matrix(y_test, y_pred)
    fig_conf_matrix = px.imshow(conf_matrix, 
                                text_auto=True, 
                                labels=dict(x="Predicción", y="Verdadero"),
                                x=["No Pagado", "Pagado"], 
                                y=["No Pagado", "Pagado"],
                                title="Matriz de Confusión")
    st.plotly_chart(fig_conf_matrix)

    st.markdown("---")
    
    # Conclusiones del modelo
    st.write("""
    ### Conclusiones
    Nuestro trabajo permite una toma de decisiones más informada. El modelo de predicción ayudará a la institución financiera a:
    
    - **Reducir riesgos:** Identificar a los clientes con mayor probabilidad de no pagar.
    - **Mejorar la eficiencia operativa:** Al automatizar la evaluación de riesgos, se acelera el proceso de aprobación.
    - **Optimizar la experiencia del cliente:** Permitir una aprobación de préstamos más rápida y personalizada.
    
    Este sistema es especialmente útil para una institución financiera que quiera ser más eficiente y precisa en la aprobación de préstamos, 
    mientras que se adapta a un mercado cada vez más digital y basado en datos.
    """)

