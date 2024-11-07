##########################################################################################################
# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import joblib
##########################################################################################################
def calcular_tasa_interes(fico_estimado, dti):
    if fico_estimado >= 750:
        tasa_base = 3.5
    elif fico_estimado >= 700:
        tasa_base = 4.0
    elif fico_estimado >= 650:
        tasa_base = 5.0
    else:
        tasa_base = 6.5

    if dti > 40:
        return tasa_base + 1.0
    elif dti < 20:
        return tasa_base - 0.5
    return tasa_base

##########################################################################################################
def Evaluacion():
    modelo = joblib.load("Data/Modelo_GradientBoosting.pkl")
    
    # Mejor threshold predefinido para recall
    best_threshold = 0.537 #podemos cambiarlo
    col1, col2 = st.columns([1, 1])
    
    ##########################################################################################################
    # Descripción e inputs del DTI
    with col1:
        loan_amnt = st.number_input("Monto del Préstamo (en €)", 1000, 50000, 10000)
        annual_inc = st.number_input("Ingreso Anual (en €)", 5000, 1000000, 75000)
        term_numeric = st.selectbox("Plazo del Préstamo (meses)", [12, 24, 36, 48, 60, 72, 84])
        total_deudas_mensuales = st.number_input("Total de Deudas Mensuales (en €)", 0.0, value=0.0)
        
        st.session_state.setdefault("dti", None)
        st.session_state.setdefault("fico_estimado", None)
        st.session_state.setdefault("tasa_interes_ajustada", None)

        # Calculadora de DTI
        if st.button("Calcular DTI"):
            if annual_inc > 0:
                ingreso_mensual = annual_inc / 12
                st.session_state.dti = (total_deudas_mensuales / ingreso_mensual) * 100
                if st.session_state.dti > 100:
                    st.error("El DTI no puede ser superior al 100%.")
            else:
                st.error("Error, revisa las cantidades introducidas.")

    ##########################################################################################################
    # Inputs y cálculos del FICO
    with col2:
        total_deudas = st.number_input("Total de Deudas (en €)", 0, value=0)
        total_credito = st.number_input("Total de Crédito Disponible (en €)", 0, value=0)
        pagos_a_tiempo = st.number_input("Pagos realizados a tiempo en el último año", 0, value=0)
        
        if st.button("Calcular Puntuación FICO Estimada"):
            credit_utilization = (total_deudas / total_credito * 100) if total_credito > 0 else 0
            st.session_state.fico_estimado = (
                850 
                - max(0, (credit_utilization - 30) * 2) 
                - max(0, (10 - pagos_a_tiempo) * 5)
            )

        if annual_inc > 0 and st.session_state.dti is not None:
            st.session_state.tasa_interes_ajustada = calcular_tasa_interes(st.session_state.fico_estimado, st.session_state.dti)

    ##########################################################################################################
    # Cálculos de variables para el modelo
    fico_range_diff = 5
    loan_income_ratio = (loan_amnt / (annual_inc / 12)) * 100 if annual_inc > 0 else 0
    fico_range_high = 850

    resultados = []

    if st.session_state.dti is not None:
        resultados.append((f"Tu DTI es:", f"{st.session_state.dti:.2f}%"))
        
    if st.session_state.fico_estimado is not None:
        resultados.append((f"Puntuación FICO estimada:", f"{st.session_state.fico_estimado:.2f}"))
        
    if st.session_state.tasa_interes_ajustada is not None:
        resultados.append((f"Tasa de Interés Calculada:", f"{st.session_state.tasa_interes_ajustada:.2f}%"))

    st.table(pd.DataFrame(resultados, columns=["Descripción", "Valor"]))

    ##########################################################################################################
    # Ajuste del threshold
    st.subheader("Ajuste de Threshold")
    threshold_usuario = st.slider("Ajusta el Threshold para la Clasificación", min_value=0.0, max_value=1.0, value=best_threshold, step=0.01)

    ##########################################################################################################
    input_datos = np.array([[fico_range_diff, loan_income_ratio, term_numeric, st.session_state.tasa_interes_ajustada]])

    # Predicción usando el threshold ajustable
    probabilidad_viabilidad = modelo.predict_proba(input_datos)[:, 1][0]
    prediccion = 1 if probabilidad_viabilidad >= threshold_usuario else 0

    st.write(f"Probabilidad de viabilidad del préstamo: {probabilidad_viabilidad:.2f}")
    if prediccion == 1:
        st.success("El préstamo que quiere solicitar es viable.")
    else:
        st.error("Lo sentimos, el préstamo no es viable.")
