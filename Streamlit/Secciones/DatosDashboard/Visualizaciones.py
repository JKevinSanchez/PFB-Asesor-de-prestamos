##########################################################################################################
# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
#########################################################################################################

df = pd.read_csv("Data/df_renombrado_limpio.csv")

#########################################################################################################

def Filtro(df):
    estado_opciones = df["Estado del Préstamo"].unique().tolist()
    estado_opciones.insert(0, "Seleccionar todo")
    
    col1, col2 = st.columns(2)

    with col1:
        estado_seleccionado = st.multiselect("Estado del préstamo:",
                                               estado_opciones,
                                               default=["Seleccionar todo"],
                                               key="estado_prestamo")

    with col2:
        proposito_opciones = df["Propósito del Préstamo"].unique().tolist()
        proposito_opciones.insert(0, "Seleccionar todo")
        proposito_seleccionado = st.multiselect("Propósito del préstamo:",
                                                 proposito_opciones,
                                                 default=["Seleccionar todo"],
                                                 key="proposito_prestamo")

    # dataframe filtrado
    if "Seleccionar todo" in estado_seleccionado:
        estado_filtrado = df
    else:
        estado_filtrado = df[df["Estado del Préstamo"].isin(estado_seleccionado)]

    if "Seleccionar todo" in proposito_seleccionado:
        proposito_filtrado = estado_filtrado
    else:
        proposito_filtrado = estado_filtrado[estado_filtrado["Propósito del Préstamo"].isin(proposito_seleccionado)]

    return proposito_filtrado

def Filtro_Histograma(df):
    estado_opciones = df["Estado del Préstamo"].unique().tolist()
    estado_opciones.insert(0, "Seleccionar todo")
    
    proposito_opciones = df["Propósito del Préstamo"].unique().tolist()
    proposito_opciones.insert(0, "Seleccionar todo")

# filtramos excluyendo ID para que no aparezca
    columnas_numericas = df.select_dtypes(include=np.number).columns.tolist()
    columnas_numericas = [col for col in columnas_numericas if col != "ID"]

# Botones de los filtros
    col1, col2, col3 = st.columns(3)

    with col1:
        columna_seleccionada = st.selectbox("Selecciona la columna:",
                                             columnas_numericas)

    with col2:
        estado_seleccionado = st.multiselect("Estado del préstamo:",
                                               estado_opciones,
                                               default=["Seleccionar todo"],
                                               key="estado_prestamo_2")

    with col3:
        proposito_seleccionado = st.multiselect("Propósito del préstamo:",
                                                 proposito_opciones,
                                                 default=["Seleccionar todo"],
                                                 key="proposito_prestamo_2")

# dataframe filtrado
    if "Seleccionar todo" in estado_seleccionado:
        estado_filtrado = df
    else:
        estado_filtrado = df[df["Estado del Préstamo"].isin(estado_seleccionado)]

    if "Seleccionar todo" in proposito_seleccionado:
        proposito_filtrado = estado_filtrado
    else:
        proposito_filtrado = estado_filtrado[estado_filtrado["Propósito del Préstamo"].isin(proposito_seleccionado)]

    return proposito_filtrado, columna_seleccionada

##########################################################################################################
# Graficos
def Violin(df):
    with st.container():
        df_filtrado = Filtro(df)

    fig = px.violin(df_filtrado, 
                     x="Propósito del Préstamo", 
                     y="Monto del Préstamo",
                     color="Propósito del Préstamo",
                     color_discrete_sequence=px.colors.qualitative.Plotly,
                     template="plotly_white")

    fig.update_traces(box_visible=True)
    fig.update_layout(title="ViolinPlot de Préstamos",
                      xaxis_title="Propósito del Préstamo",
                      yaxis_title="Monto del Préstamo",
                      plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)')

    st.plotly_chart(fig)

##########################################################################################################

def Boxplot(df):
    with st.container():
        df_filtrado = Filtro(df)

    fig = px.box(df_filtrado, 
                     x="Propósito del Préstamo", 
                     y="Monto del Préstamo",
                     color="Propósito del Préstamo",
                     color_discrete_sequence=px.colors.qualitative.Plotly,
                     template="plotly_white")

    fig.update_layout(title="Boxplot de Préstamos",
                      xaxis_title="Propósito del Préstamo",
                      yaxis_title="Monto del Préstamo",
                      plot_bgcolor="rgba(0,0,0,0)",
                      paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig)

##########################################################################################################

def Histograma(df, columna_seleccionada):
    with st.container():
        df_hist, columna_seleccionada = Filtro_Histograma(df)

    fig = px.histogram(df_hist, 
                        x=columna_seleccionada, 
                        color="Estado del Préstamo",
                        barmode="overlay",
                        template="plotly_white")

    fig.update_layout(title=f"Histograma de {columna_seleccionada}",
                      xaxis_title=columna_seleccionada,
                      yaxis_title="Frecuencia",
                      plot_bgcolor="rgba(0,0,0,0)",
                      paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig)

##########################################################################################################

def Grafico_Dispersion_3D(df):
    Desc_Dispersion3D()

    variables = df.select_dtypes(include=[np.number]).columns.tolist()
    variables.remove("ID") if "ID" in variables else None

#########################
# Inputs del usuario
    col1, col2, col3 = st.columns(3)
    with col1:
        x_var = st.selectbox("Selecciona la variable para el eje X:", options=variables)
    with col2:
        y_var = st.selectbox("Selecciona la variable para el eje Y:", options=[var for var in variables if var != x_var])
    with col3:
        z_var = st.selectbox("Selecciona la variable para el eje Z:", options=[var for var in variables if var not in [x_var, y_var]])

    estado_options = ["Seleccionar todo"] + df["Estado del Préstamo"].unique().tolist()
    estados_seleccionados = st.multiselect(
        "Selecciona el/los estado(s) del préstamo:", 
        options=estado_options, 
        default=["Seleccionar todo"]
    )

#########################
# manejo del input y mostrar fig
    if "Seleccionar todo" in estados_seleccionados:
        estados_seleccionados = estado_options[1:]

    if x_var and y_var and z_var:
        fig = px.scatter_3d(
            df[df["Estado del Préstamo"].isin(estados_seleccionados)], 
            x=x_var, 
            y=y_var, 
            z=z_var,
            color='Estado del Préstamo',
            labels={x_var: x_var,
                    y_var: y_var,
                    z_var: z_var},
            height = 600,
            width = 1700
            )
        
        fig.update_traces(showlegend=False)
        
        st.plotly_chart(fig)
    else:
        st.warning("Por favor, selecciona variables para todos los ejes.")

##########################################################################################################
##########################################################################################################
# Descripciones

def Desc_BoxViolin():
    st.markdown("<div class='tab-content'>Visualizaciones.</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<h2 style='color: violet; font-weight: bold;'>Diagrama de Violin y Diagrama de Caja y Bigotes</h2>", unsafe_allow_html=True)
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("""
        <p class="big-font">
        Los Diagramas de Violin y de Caja y Bigotes son herramientas para <strong style='color: violet; font-weight: bold;'>analizar la distribución</strong> de datos, facilitando la identificación de patrones y valores atípicos en diferentes conjuntos de información.
        </p>
        <p class="big-font">
        <strong style='color: violet; font-weight: bold;'>Violin Plot:</strong> Este gráfico muestra la <strong style='color: violet; font-weight: bold;'>densidad</strong> de los datos, permitiendo ver <strong style='color: violet; font-weight: bold;'>cómo se distribuyen</strong> en general. Ayuda a identificar grupos y patrones en diversas categorías.
        </p>
        <p class="big-font">
        <strong style='color: violet; font-weight: bold;'>Box Plot:</strong> Este gráfico ilustra los <span style='color: violet; text-decoration: underline; cursor: pointer;' title='Los cuartiles dividen los datos en cuatro partes iguales.'>cuartiles</span> y <span style='color: violet; text-decoration: underline; cursor: pointer;' title='Los valores atípicos son aquellos que se alejan significativamente de la mayoría de los datos.'>valores atípicos</span>, ofreciendo una visión clara de la <span style='color: violet; text-decoration: underline; cursor: pointer;' title='La mediana es el valor central de los datos.'>mediana</span> y la <span style='color: violet; text-decoration: underline; cursor: pointer;' title='La variabilidad indica cuán dispersos están los datos alrededor de la mediana.'>variabilidad</span>. Es útil para detectar valores inusuales y comparar diferentes grupos.
        </p>
        <p class="big-font">
        Juntos, estos gráficos ayudan a entender el comportamiento de los datos y a tomar mejores decisiones gracias al análisis visual que aportan.
        </p>

        """, unsafe_allow_html=True)
        
    with col2:
        graficos = st.radio("Selecciona el tipo de gráfico:", ("ViolinPlot", "BoxPlot"))

        if graficos == "ViolinPlot":
            Violin(df)
        else:
            Boxplot(df)

##########################################################################################################

def Desc_Histograma():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Histograma</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col3, col4 = st.columns([1, 1])
    with col3:
        with st.expander("¿Qué hace el histograma?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        Un <strong style='color: violet; font-weight: bold;'>histograma</strong> es una herramienta gráfica que permite <strong style='color: violet; font-weight: bold;'>visualizar la distribución</strong> de un conjunto de datos. En el contexto de los préstamos, muestra cómo se distribuyen las, <strong style='color: violet; font-weight: bold;'>variables</strong> o en este caso, la <strong style='color: violet; font-weight: bold;'>columna</strong> que selecciones en diferentes rangos.
        </p>
        <p class="big-font">
        Facilita la identificación de <strong style='color: violet; font-weight: bold;'>patrones</strong>, <strong style='color: violet; font-weight: bold;'>tendencias</strong> y posibles <strong style='color: violet; font-weight: bold;'>anomalías</strong> en los datos de préstamos.
        </p>
        """, unsafe_allow_html=True)
    with col4:
        with st.expander("¿Para qué sirve el histograma?", expanded=False):
            st.markdown("""
        <p class="big-font">
        El <strong style='color: violet; font-weight: bold;'>histograma</strong> ayuda en el análisis de riesgo, la toma de decisiones y la identificación de tendencias en los préstamos. 
        </p>
        <p class="big-font">
        Al visualizar cómo se distribuyen los montos de los préstamos, podemos <strong style='color: violet; font-weight: bold;'>evaluar riesgos</strong> y <strong style='color: violet; font-weight: bold;'>segmentar clientes</strong> por ejemplo, según sus necesidades.
        </p>
        <p class="big-font">
        Además, esta visualización, permite a los prestatarios y prestamistas establecer <strong style='color: violet; font-weight: bold;'>expectativas realistas</strong> sobre los montos que se otorgan, mejorando así la <strong style='color: violet; font-weight: bold;'>comunicación</strong> y la <strong style='color: violet; font-weight: bold;'>confianza</strong>.
        </p>
        """, unsafe_allow_html=True)

    st.markdown(""" 
    <p class="big-font">
    Puedes seleccionar la columna de interés para ver cómo se distribuyen los datos y aplicar filtros adicionales para refinar la visualización.
    </p>
    """, unsafe_allow_html=True)

##########################################################################################################
def Desc_Dispersion3D():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Gráfico de Dispersión 3D</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        with st.expander("¿Qué hace el gráfico de dispersión 3D?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        Un <strong style='color: violet; font-weight: bold;'>gráfico de dispersión 3D</strong> es una representación visual que muestra la relación entre <strong style='color: violet; font-weight: bold;'>tres variables numéricas</strong> en un espacio tridimensional. Cada <strong style='color: violet; font-weight: bold;'>punto</strong> en el gráfico representa <strong style='color: violet; font-weight: bold;'>un registro</strong> en el conjunto de datos, y su posición está determinada por los valores de las variables seleccionadas para los ejes <strong style='color: violet; font-weight: bold;'>X, Y y Z</strong>.
        </p>
        <p class="big-font">
        Esta visualización facilita la identificación de <strong style='color: violet; font-weight: bold;'>patrones</strong>, <strong style='color: violet; font-weight: bold;'>tendencias</strong> y <strong style='color: violet; font-weight: bold;'>relaciones</strong> entre las variables.
        </p>
        """, unsafe_allow_html=True)
    
    with col2:
        with st.expander("¿Para qué sirve el gráfico de dispersión 3D?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        El <strong style='color: violet; font-weight: bold;'>gráfico de dispersión 3D</strong> sirve para <strong style='color: violet; font-weight: bold;'>analizar</strong> las <strong style='color: violet; font-weight: bold;'>interacciones</strong> entre múltiples variables de una manera <strong style='color: violet; font-weight: bold;'>innovadora</strong> y <strong style='color: violet; font-weight: bold;'>muy visual</strong>. 
        </p>
        <p class="big-font">
        Permite a los analistas detectar <strong style='color: violet; font-weight: bold;'>anomalías</strong> en los datos, entender cómo varían las <strong style='color: violet; font-weight: bold;'>variables</strong> entre sí y evaluar su impacto en el <strong style='color: violet; font-weight: bold;'>resultado del préstamo</strong>.
        </p>
        """, unsafe_allow_html=True)

    with col3:
        with st.expander("¿Cómo utilizo el gráfico de dispersión 3D?", expanded=False):
            st.markdown(""" 
        <p class="big-font">
        Para utilizar el <strong style='color: violet; font-weight: bold;'>Gráfico de Dispersión 3D</strong>, selecciona una <strong style='color: violet; font-weight: bold;'>variable</strong> para cada uno de los ejes <strong style='color: violet; font-weight: bold;'>X, Y y Z</strong>. Ten en cuenta que <strong style='color: violet; font-weight: bold;'>no podrás</strong> seleccionar la <strong style='color: violet; font-weight: bold;'>misma variable</strong> en más de un eje.
        </p>
        <p class="big-font">
        Una vez <strong style='color: violet; font-weight: bold;'>seleccionadas</strong> las <strong style='color: violet; font-weight: bold;'>variables</strong>, el gráfico se actualizará automáticamente para mostrar la <strong style='color: violet; font-weight: bold;'>relación</strong> entre ellas. Puedes explorar <strong style='color: violet; font-weight: bold;'>cómo se distribuyen</strong> los datos y buscar <strong style='color: violet; font-weight: bold;'>correlaciones</strong> o <strong style='color: violet; font-weight: bold;'>patrones</strong> que puedan influir en el <strong style='color: violet; font-weight: bold;'>análisis de riesgos</strong> y la <strong style='color: violet; font-weight: bold;'>toma de decisiones</strong>.
        </p>
        """, unsafe_allow_html=True)

    st.markdown(""" 
    <p class="big-font">
    Recuerda que al elegir <strong style='color: violet; font-weight: bold;'>variables significativas</strong>, el gráfico proporcionará <strong style='color: violet; font-weight: bold;'>información más relevante</strong> para el análisis de tus datos:
    </p>
    """, unsafe_allow_html=True)