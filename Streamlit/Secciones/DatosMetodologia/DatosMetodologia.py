
import streamlit as st


def Metod():
    st.markdown("<div class='tab-content'>Metodología.</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown(""" 
    <p class="big-font">
    Para organizar el trabajo de este proyecto, utilizamos una <strong style='color: violet; font-weight: bold;'>metodología ágil</strong> llamada <strong style='color: violet; font-weight: bold;'>Scrum</strong>.
    </p>
    <p class="big-font"> 
    <strong style='color: violet; font-weight: bold;'>Scrum</strong> es un enfoque que permite <strong style='color: violet; font-weight: bold;'>dividir</strong> el proyecto en tareas <strong style='color: violet; font-weight: bold;'>más pequeñas y manejables</strong>, denominadas <em><strong style='color: violet; font-weight: bold;'>sprints</strong></em>. 
    </p>
    <p class="big-font">           
    Cada <em><strong style='color: violet; font-weight: bold;'>sprint</strong></em> tiene una duración fija</strong> (en este caso, dos semanas), y al final de cada <em><strong style='color: violet; font-weight: bold;'>sprint</strong></em>, <strong style='color: violet; font-weight: bold;'>evaluamos el progreso</strong> y <strong style='color: violet; font-weight: bold;'>hacemos ajustes</strong> según sea <strong style='color: violet; font-weight: bold;'>necesario</strong> y nos hayan <strong style='color: violet; font-weight: bold;'>indicado</strong>.
    </p>
    <p class="big-font"> 
    Esto nos ayuda a <strong style='color: violet; font-weight: bold;'>adaptarnos</strong> a los cambios de <strong style='color: violet; font-weight: bold;'>forma rápida</strong> y a <strong style='color: violet; font-weight: bold;'>mejorar continuamente</strong>, asegurándonos de que el <strong style='color: violet; font-weight: bold;'>proyecto evoluciona</strong> en la dirección correcta a medida que recibimos <strong style='color: violet; font-weight: bold;'>comentarios y nuevos conocimientos</strong>.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .container {
        border: 5px solid violet;
        border-radius: 15px;
        padding: 10px;
        text-align: center;
        background-color: #f9f9f9;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    <div class="container">
        <img src='https://www.pixelgrafia.com/images/development/scrum.gif' alt='animated' width='700'/>
    </div>
    """, unsafe_allow_html=True)

def Resultados():

    st.markdown("<div class='tab-content'>Resultados.</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, separador, col2 = st.columns((1, 0.1, 1))
    with col1:
        st.markdown("""
        <p class="big-font">
        <strong style='color: violet; font-size: 30px; font-weight: bold;'>¿Qué Modelo de Machine Learning hemos utilizado?</strong>
        </p>
        <p class="big-font">
        Para determinar la viabilidad de los préstamos, optamos por un modelo de <strong style='color: violet; font-weight: bold;'>aprendizaje automático</strong> conocido como <strong style='color: violet; font-weight: bold;'>Gradient Boosting Classifier</strong>. Este modelo opera mediante una serie de <strong style='color: violet; font-weight: bold;'>árboles de decisión</strong>, que podemos imaginar como <strong style='color: violet; font-weight: bold;'>secuencias de preguntas</strong> que el modelo utiliza para entender los datos.
        </p>
        <p class="big-font">
        Cada árbol plantea interrogantes como: <em><strong style='color: violet; font-weight: bold;'>"¿El ingreso anual supera cierto umbral?"</strong></em> o <em><strong style='color: violet; font-weight: bold;'>"¿El cliente utiliza menos del 30% de su crédito?"</strong></em>. La magia radica en que cada árbol <strong style='color: violet; font-weight: bold;'>intenta mejorar</strong> la predicción del anterior, similar a un equipo de entrenadores trabajando juntos para afinar su estrategia y lograr decisiones más acertadas.
        </p>
        """, unsafe_allow_html=True)
    with separador:
        st.markdown("<div class='vertical-separator'></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <p class="big-font">
        <strong style='color: violet;font-size: 30px; font-weight: bold;'>¿Por qué es útil el Gradient Boosting?</strong>
        </p>          
        <p class="big-font">
        Porque el modelo <strong style='color: violet; font-weight: bold;'>aprende de sus errores</strong>. Cuando un árbol falla en su predicción, el siguiente se enfoca en <strong style='color: violet; font-weight: bold;'>corregir</strong> esos fallos, lo que da como resultado un modelo <strong style='color: violet; font-weight: bold;'>cada vez más preciso</strong>. Esta característica es crucial para diferenciar entre clientes que <strong style='color: violet; font-weight: bold;'>probablemente pagarán</strong> y aquellos que presentan un <strong style='color: violet; font-weight: bold;'>mayor riesgo de impago</strong>.
        </p>
        <p class="big-font">
        Además, el <strong style='color: violet; font-weight: bold;'>Gradient Boosting</strong> es <strong style='color: violet; font-weight: bold;'>extremadamente flexible</strong> y puede adaptarse a diferentes tipos de <strong style='color: violet; font-weight: bold;'>datos</strong> y <strong style='color: violet; font-weight: bold;'>problemas</strong>. Esto significa que no solo es eficaz en la clasificación, sino que también se puede utilizar para <strong style='color: violet; font-weight: bold;'>regresión</strong> y otras <strong style='color: violet; font-weight: bold;'>tareas predictivas</strong>. Su capacidad para manejar <strong style='color: violet; font-weight: bold;'>interacciones complejas</strong> entre variables lo convierte en una <strong style='color: violet; font-weight: bold;'>herramienta poderosa</strong> en el arsenal del análisis de datos.
        </p>
        """, unsafe_allow_html=True)

def Conclusiones():

    st.markdown("<div class='tab-content'>Conclusiones.</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown(""" 
    <p class="big-font">
    Nuestro trabajo permite una mejora en la <strong style='color: violet; font-weight: bold;'>toma de decisiones</strong>. El modelo de predicción puede ayudar a las instituciones financieras a:
    </p>
    <p class="big-font">
    - <strong style='color: violet; font-weight: bold;'>Reducir riesgos:</strong> Identificar a los clientes con mayor probabilidad de <strong style='color: violet; font-weight: bold;'>no pagar</strong>.
    </p>
    <p class="big-font">
    - <strong style='color: violet; font-weight: bold;'>Mejorar la eficiencia operativa:</strong> Al automatizar la evaluación de riesgos, se acelera el proceso de <strong style='color: violet; font-weight: bold;'>aprobación</strong>.
    </p>
    <p class="big-font">
    - <strong style='color: violet; font-weight: bold;'>Optimizar la experiencia del cliente:</strong> Permitir un análisis y una aprobación de préstamos más <strong style='color: violet; font-weight: bold;'>rápida</strong> y <strong style='color: violet; font-weight: bold;'>personalizada</strong>.
    </p>
    <p class="big-font">
    Este sistema es especialmente útil para una <strong style='color: violet; font-weight: bold;'>institución financiera</strong> que quiera ser más <strong style='color: violet; font-weight: bold;'>eficiente</strong> y <strong style='color: violet; font-weight: bold;'>precisa</strong> en la aprobación de préstamos, mientras se adapta a un mercado cada vez más <strong style='color: violet; font-weight: bold;'>digital</strong> y <strong style='color: violet; font-weight: bold;'>basado en datos</strong>.
    </p>
    """, unsafe_allow_html=True)