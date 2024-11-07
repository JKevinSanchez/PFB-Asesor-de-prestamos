##########################################################################################################
# Librerias
import streamlit as st
import streamlit_folium
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
##########################################################################################################

def Evaluacion():
    modelo = joblib.load("Data/Modelo_GradientBoosting.pkl")

    col1, col2 = st.columns([1, 1])
    
    ##########################################################################################################
    # Descripción e inputs del DTI
    with col1:
        Desc_DTI()
        loan_amnt = st.number_input("Monto del Préstamo (en €)", 1000, 50000, 10000)
        annual_inc = st.number_input("Ingreso Anual (en €)", 5000, 1000000, 75000)
        term_numeric = st.selectbox("Plazo del Préstamo (meses)", [12, 24, 36, 48, 60, 72, 84])
        total_deudas_mensuales = st.number_input("Total de Deudas Mensuales (en €)", 0.0, value=50.0)

    ##########################################################################################################
    # Guardar datos para la evaluación
    st.session_state.setdefault("dti", None)
    st.session_state.setdefault("fico_estimado", None)
    st.session_state.setdefault("tasa_interes_ajustada", None)

    ##########################################################################################################
    # Calculadora de DTI
    if st.button("Calcular DTI"):
        if annual_inc > 0:
            ingreso_mensual = annual_inc / 12
            st.session_state.dti = (total_deudas_mensuales / ingreso_mensual) * 100
            if st.session_state.dti > 100:
                st.error("El DTI no puede ser superior al 100%.")
        else:
            st.error("Error, revisa las cantidades introducidas.")

    st.markdown("<hr>", unsafe_allow_html=True)

    ##########################################################################################################
    # Descripción e inputs del FICO
    with col2:
        Desc_FICO()
        total_deudas = st.number_input("Total de Deudas (en €)", 0, value=0)
        total_credito = st.number_input("Total de Crédito Disponible (en €)", 0, value=0)
        pagos_a_tiempo = st.number_input("Pagos realizados a tiempo en el último año", 0, value=0)

    ##########################################################################################################
    # Cálculos para el FICO
        if st.button("Calcular Puntuación FICO Estimada"):
            if total_credito > 0:
                credit_utilization = (total_deudas / total_credito) * 100
                st.session_state.fico_estimado = (
                    850 
                    - max(0, (credit_utilization - 30) * 2) 
                    - max(0, (10 - pagos_a_tiempo) * 5)
                )
            else:
                st.error("Error, el Total de Crédito Disponible debe ser mayor a cero.")

        if annual_inc > 0 and st.session_state.dti is not None and st.session_state.fico_estimado is not None:
            st.session_state.tasa_interes_ajustada = calcular_tasa_interes(st.session_state.fico_estimado, st.session_state.dti)

    ##########################################################################################################
    # Calculamos las relaciones necesarias
    fico_range_diff = 5
    loan_income_ratio = (loan_amnt / (annual_inc / 12)) * 100 if annual_inc > 0 else 0
    fico_range_high = 850

    ##########################################################################################################
    # Tabla de resultados para que el usuario lo vea
    resultados = []

    if st.session_state.dti is not None:
        resultados.append((f"Tu DTI es:", f"{st.session_state.dti:.2f}%"))
        
    if st.session_state.fico_estimado is not None:
        resultados.append((f"Puntuación FICO estimada:", f"{st.session_state.fico_estimado:.2f}"))
        
    if st.session_state.tasa_interes_ajustada is not None:
        resultados.append((f"Tasa de Interés Calculada:", f"{st.session_state.tasa_interes_ajustada:.2f}%"))

    resultados.append((f"Rango FICO Diferencia:", f"{fico_range_diff:.2f}"))
    resultados.append((f"Relación Préstamo-Ingreso:", f"{loan_income_ratio:.2f}%"))

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Tus Resultados según los Datos introducidos:</h3>", unsafe_allow_html=True)

    cols = st.columns(len(resultados))

    for col, (descripcion, valor) in zip(cols, resultados):
        with col:
            st.markdown(
                f"<div style='background-color: #9b59b6; font-weight: bold; padding: 10px; border-radius: 5px; text-align: center;'>"
                f"<strong>{descripcion}</strong><br>{valor}</div>", 
                unsafe_allow_html=True
            )

    st.markdown("", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    ##########################################################################################################
    # Ajuste del threshold y boton para que el usuario pueda reestablecerlo al mejor threshold
    mejor_threshold = 0.537

    Desc_Threshold()

    if "threshold_usuario" not in st.session_state:
        st.session_state.threshold_usuario = mejor_threshold

    if "reset_threshold" not in st.session_state:
        st.session_state.reset_threshold = False

    col3, col4 = st.columns((3, 1))

    with col3:
        threshold_usuario = st.slider(label="a",
                                    label_visibility="hidden",
                                    min_value=0.000,
                                    max_value=1.000,
                                    value=mejor_threshold if st.session_state.reset_threshold else st.session_state.threshold_usuario,
                                    step=0.001,
                                    format="%.3f",
                                    key="threshold_slider")
        st.session_state.threshold_usuario = threshold_usuario

    with col4:
        if st.button("Volver al Threshold más óptimo (Haz Doble Click Aquí)"):
            st.session_state.threshold_usuario = mejor_threshold
            st.session_state.reset_threshold = True

    if st.session_state.reset_threshold:
        st.session_state.reset_threshold = False

    ##########################################################################################################
    # Evaluación del préstamo
    if st.button("Evaluar Préstamo"):
        if st.session_state.tasa_interes_ajustada is None:
            st.error("Por favor, calcula primero el DTI y la Puntuación FICO.")
        elif st.session_state.dti is None or st.session_state.fico_estimado is None:
            st.error("Por favor, asegúrate de calcular tanto el DTI como la Puntuación FICO.")
        else:
            input_datos = {
                "fico_range_diff": [fico_range_diff],
                "loan_income_ratio": [loan_income_ratio],
                "term_numeric": [term_numeric],
                "interest_loan": [st.session_state.tasa_interes_ajustada],
                "loan_amnt": [loan_amnt],
                "annual_inc": [annual_inc],
                "int_rate": [st.session_state.tasa_interes_ajustada],
                "fico_range_high": [fico_range_high]
            }

            input_datos_df = pd.DataFrame(input_datos)

            prediccion = modelo.predict(input_datos_df)
            probabilidad = modelo.predict_proba(input_datos_df)[:, 1]

            if probabilidad[0] >= threshold_usuario:
                st.success("¡Felicidades! El préstamo que quieres solicitar es viable, póngase en contacto con nosotros para realizar los trámites necesarios.")
                Exito(loan_amnt, annual_inc, total_deudas_mensuales, st.session_state.fico_estimado, st.session_state.tasa_interes_ajustada, loan_income_ratio, st.session_state.dti)
            else:
                st.error("Lo sentimos, el préstamo no es viable, prueba a solicitar una cantidad distinta o no dudes en consultarnos para un análisis más exhaustivo.")

    ##########################################################################################################
    # Muestreo de los datos para la predicción del usuario
            st.markdown("<h3 style='text-align: center;'>Datos Utilizados para la Predicción:</h3>", unsafe_allow_html=True)

            traducciones = {
                "fico_range_diff": "Diferencia FICO",
                "loan_income_ratio": "Tasa Préstamo-Ingreso",
                "term_numeric": "Plazo del Préstamo",
                "interest_loan": "Tasa de Interés",
                "loan_amnt": "Monto del Préstamo",
                "annual_inc": "Ingreso Anual",
                "int_rate": "Tasa de Interés",
                "fico_range_high": "Rango FICO Alto"
            }

            datos = [(traducciones[col], input_datos_df[col][0]) for col in input_datos_df.columns]

            cols = st.columns(len(datos))

            for col, (descripcion, valor) in zip(cols, datos):
                with col:
                    st.markdown(
                        f"<div style='background-image: url(https://i.ibb.co/7NM1Ln7/9150117.jpg); background-color: rgba(128, 0, 128, 0.7); font-weight: bold; padding: 15px; border-radius: 5px; text-align: center;'>"
                        f"<strong>{descripcion}:</strong><br>{valor:.3f}</div>", 
                        unsafe_allow_html=True
                    )

            st.markdown("", unsafe_allow_html=True)

if __name__ == "__main__":
    Evaluacion()


##########################################################################################################
##########################################################################################################

def Desc_DTI():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Razón Deuda-Ingreso (DTI)</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        with st.expander("¿Qué es el DTI?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        La <strong style='color: violet; font-weight: bold;'>Razón Deuda-Ingreso (DTI)</strong> es una métrica financiera que compara los <strong style='color: violet; font-weight: bold;'>ingresos mensuales</strong> de un prestatario con sus <strong style='color: violet; font-weight: bold;'>obligaciones de deuda</strong>. Se expresa como un porcentaje y es fundamental para los prestamistas al evaluar la capacidad de un solicitante para asumir un nuevo préstamo.
        </p>
        <p class="big-font">
        Un <strong style='color: violet; font-weight: bold;'>DTI bajo</strong> sugiere que el prestatario tiene un <strong style='color: violet; font-weight: bold;'>margen financiero</strong> para manejar más deuda, mientras que un <strong style='color: violet; font-weight: bold;'>DTI alto</strong> puede indicar un <strong style='color: violet; font-weight: bold;'>mayor riesgo</strong> de incumplimiento.
        </p>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.expander("¿Por qué es importante el DTI?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        El DTI es una herramienta crucial en la <strong style='color: violet; font-weight: bold;'>evaluación del riesgo crediticio</strong>. Permite a los prestamistas entender la carga de deuda de un prestatario en relación con sus ingresos, ayudando a <strong style='color: violet; font-weight: bold;'>determinar la viabilidad</strong> de conceder un préstamo.
        </p>
        <p class="big-font">
        Además, los prestatarios pueden utilizar su DTI para <strong style='color: violet; font-weight: bold;'>gestionar sus finanzas</strong> y hacer ajustes si es necesario, mejorando así su <strong style='color: violet; font-weight: bold;'>situación financiera general</strong> y su capacidad para acceder a <strong style='color: violet; font-weight: bold;'>financiamiento</strong> en el futuro.
        </p>
        """, unsafe_allow_html=True)
    
    with col3:
        with st.expander("¿Cómo se calcula el DTI?", expanded=False):
            st.markdown("""
            <p class="big-font">
            El <strong style='color: violet; font-weight: bold;'>DTI</strong> se calcula dividiendo el <strong style='color: violet; font-weight: bold;'>total de deudas mensuales</strong> por el <strong style='color: violet; font-weight: bold;'>ingreso mensual</strong>, y multiplicando el resultado por 100 para obtener un porcentaje, además pedimos el <strong style='color: violet; font-weight: bold;'>plazo del préstamo deseado</strong>, para sacar un <strong style='color: violet; font-weight: bold;'>aproximado</strong>, del <strong style='color: violet; font-weight: bold;'>interés</strong>.
            </p>
            <p class="big-font">
            Fórmula: <strong style='color: violet;'>DTI (%) = (Deudas Mensuales / Ingreso Mensual) * 100</strong>.
            </p>
            """, unsafe_allow_html=True)
            
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown(""" 
    <p class="big-font">
    Un <strong style='color: violet; font-weight: bold;'>DTI</strong> idealmente se mantiene por debajo del <strong style='color: violet; font-weight: bold;'>36%</strong>, aunque <strong style='color: violet; font-weight: bold;'>algunas instituciones financieras</strong> pueden considerar aceptable un <strong style='color: violet; font-weight: bold;'>DTI</strong> de hasta <strong style='color: violet; font-weight: bold;'>43%</strong> o más, dependiendo de otros factores.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

##########################################################################################################

def Desc_FICO():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Puntuación de Crédito FICO</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        with st.expander("¿Qué es la Puntuación FICO?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        La <strong style='color: violet; font-weight: bold;'>Puntuación FICO</strong> es un número que representa la <strong style='color: violet; font-weight: bold;'>capacidad crediticia</strong> de un individuo, basado en su historial crediticio. Las puntuaciones FICO varían de <strong style='color: violet; font-weight: bold;'>300 a 850</strong>, donde un número <strong style='color: violet; font-weight: bold;'>más alto</strong> indica un <strong style='color: violet; font-weight: bold;'>menor riesgo</strong> para los prestamistas.
        </p>
        <p class="big-font">
        Los factores que afectan la puntuación incluyen el <strong style='color: violet; font-weight: bold;'>historial de pagos</strong>, la <strong style='color: violet; font-weight: bold;'>cantidad de deuda total</strong>, el <strong style='color: violet; font-weight: bold;'>historial crediticio</strong>, el <strong style='color: violet; font-weight: bold;'>crédito disponible</strong>, entre otros.
        </p>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.expander("¿Por qué es importante el FICO?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        La puntuación FICO es un elemento clave en la <strong style='color: violet; font-weight: bold;'>evaluación de crédito</strong> y puede influir en las tasas de interés, la aprobación del préstamo y los términos del crédito. Una <strong style='color: violet; font-weight: bold;'>puntuación alta</strong> puede resultar en <strong style='color: violet; font-weight: bold;'>mejores ofertas</strong> de préstamos.
        </p>
        <p class="big-font">
        Además, <strong style='color: violet; font-weight: bold;'>comprender</strong> y <strong style='color: violet; font-weight: bold;'>monitorear</strong> la puntuación FICO puede ayudar a los consumidores a tomar <strong style='color: violet; font-weight: bold;'>mejores decisiones</strong> sobre sus finanzas y a mejorar su <strong style='color: violet; font-weight: bold;'>situación crediticia</strong> con el tiempo.
        </p>
        """, unsafe_allow_html=True)
    
    with col3:
        with st.expander("¿Cómo se calcula el FICO?", expanded=False):
            st.markdown("""
            <p class="big-font">
            En este modelo, la <strong style='color: violet; font-weight: bold;'>Puntuación FICO</strong> se utiliza como uno de los indicadores clave de la <strong style='color: violet; font-weight: bold;'>viabilidad del préstamo</strong>. Factores como el <strong style='color: violet; font-weight: bold;'>historial de pagos</strong> y el <strong style='color: violet; font-weight: bold;'>nivel de deuda</strong> del solicitante afectan esta <strong style='color: violet; font-weight: bold;'>puntuación</strong>.
            </p>
            <p class="big-font">
            Aquí, el <strong style='color: violet; font-weight: bold;'>FICO</strong> se considera en combinación con otras características para analizar la <strong style='color: violet; font-weight: bold;'>probabilidad de pago</strong> del préstamo, <strong style='color: violet; font-weight: bold;'>no siendo un cálculo directo</strong>.
            </p>
            """, unsafe_allow_html=True)
            
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown(""" 
    <p class="big-font">
    Las <strong style='color: violet; font-weight: bold;'>puntuaciones FICO</strong> por encima de <strong style='color: violet; font-weight: bold;'>700</strong> se consideran buenas, mientras que una puntuación de <strong style='color: violet; font-weight: bold;'>800</strong> o más es <strong style='color: violet; font-weight: bold;'>excelente</strong>.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
##########################################################################################################

def Desc_Threshold():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Ajuste de Threshold</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("""
    <p class="big-font">
    Gracias a nuestro estudio, hemos definido que el <strong style='color: violet; font-weight: bold;'>mejor threshold</strong> es <strong style='color: violet; font-weight: bold;'>0.537</strong>, optimizando así la clasificación de viabilidad del préstamo. Este valor proporciona un <strong style='color: violet; font-weight: bold;'>equilibrio ideal</strong> entre <strong style='color: violet; font-weight: bold;'>precisión</strong> y <strong style='color: violet; font-weight: bold;'>sensibilidad</strong> en nuestras <strong style='color: violet; font-weight: bold;'>predicciones</strong>.
    </p>
    <p class="big-font">
    Te <strong style='color: violet; font-weight: bold;'>recomendamos encarecidamente</strong> que, aunque te damos la opción de modificar el threshold para <strong style='color: violet; font-weight: bold;'>comprobar</strong> cómo cambian los resultados, a la hora de <strong style='color: violet; font-weight: bold;'>evaluar un préstamo</strong>, <strong style='color: violet; font-weight: bold;'>mantengas el Threshold más óptimo: 0.537</strong>, para <strong style='color: violet; font-weight: bold;'>mayor precisión</strong> y <strong style='color: violet; font-weight: bold;'>realismo</strong> en los resultados.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns((1, 1))

    with col1:
        with st.expander("¿Qué es un Threshold?", expanded=False):
            st.markdown("""
            <p class="big-font">
            Un <strong style='color: violet; font-weight: bold;'>threshold</strong> es un valor de corte que define el límite a partir del cual una predicción se clasifica en una categoría u otra, por ejemplo, en <strong style='color: violet; font-weight: bold;'>aprobado</strong> o <strong style='color: violet; font-weight: bold;'>rechazado</strong>.
            </p>
            """, unsafe_allow_html=True)

    with col2:
        with st.expander("¿Para qué sirve el Threshold en este caso?", expanded=False):
            st.markdown("""
            <p class="big-font">
            En nuestro modelo, el threshold de <strong>0.537</strong> se utiliza para determinar si un préstamo es <strong style='color: violet; font-weight: bold;'>viable</strong> o <strong style='color: violet; font-weight: bold;'>no viable</strong>. Ajustarlo permite controlar la precisión y reducir el riesgo en las decisiones de crédito.
            </p>
            """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)


##########################################################################################################

def Exito(loan_amnt, annual_inc, total_deudas_mensuales, fico_estimado, tasa_interes_ajustada, loan_income_ratio, dti):
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<div class='tab-content'>Análisis del Préstamo.</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    
    st.markdown("""
    <p class="big-font">
    A continuación, te mostramos por qué tu <strong style='color: violet; font-weight: bold;'>Préstamo</strong> es <strong style='color: violet; font-weight: bold;'>viable</strong> y en qué nos hemos basado para <strong style='color: violet; font-weight: bold;'>evaluar su viabilidad</strong>.
    </p>
    <p class="big-font">
    Con un <strong style='color: violet; font-weight: bold;'>monto del préstamo</strong> de €{:.2f}, un <strong style='color: violet; font-weight: bold;'>ingreso anual</strong> de €{:.2f}, y un <strong style='color: violet; font-weight: bold;'>total de deudas mensuales</strong> de €{:.2f}, nuestro modelo ha calculado lo siguiente:
    </p>
    <p class="big-font">
    - <strong style='color: violet; font-weight: bold;'>DTI (Ratio de Deuda a Ingreso)</strong>: {:.2f}%. Un DTI <strong style='color: violet; font-weight: bold;'>por debajo del 36%</strong> generalmente indica una <strong style='color: violet; font-weight: bold;'>carga de deuda manejable</strong>.
    </p>
    <p class="big-font">
    - <strong style='color: violet; font-weight: bold;'>Puntuación FICO Estimada</strong>: {:.2f}. Una puntuación de FICO <strong style='color: violet; font-weight: bold;'>superior a 700</strong> generalmente indica un <strong style='color: violet; font-weight: bold;'>buen comportamiento crediticio</strong>.
    </p>
    <p class="big-font">
    - <strong style='color: violet; font-weight: bold;'>Tasa de Interés Ajustada</strong>: {:.2f}%. La tasa de interés que se ha calculado, se considera <strong style='color: violet; font-weight: bold;'>competitiva en el mercado</strong>.
    </p>
    <p class="big-font">
    La <strong style='color: violet; font-weight: bold;'>relación préstamo-ingreso</strong> calculada es {:.2f}%, lo que indica que el monto solicitado es <strong style='color: violet; font-weight: bold;'>razonable</strong> en <strong style='color: violet; font-weight: bold;'>comparación con tu ingreso</strong>. Esto, combinado con tu <strong style='color: violet; font-weight: bold;'>buen DTI</strong> y una <strong style='color: violet; font-weight: bold;'>sólida puntuación FICO</strong>, sugiere que es probable que puedas <strong style='color: violet; font-weight: bold;'>manejar el préstamo de manera efectiva</strong>.
    </p>
    <p class="big-font">
    <strong style='color: violet; font-weight: bold;'>Por estas razones, el préstamo que deseas solicitar es viable. ¡Felicidades!</strong>
    </p>
    """.format(loan_amnt, annual_inc, total_deudas_mensuales, dti, fico_estimado, tasa_interes_ajustada, loan_income_ratio), unsafe_allow_html=True)

##########################################################################################################

