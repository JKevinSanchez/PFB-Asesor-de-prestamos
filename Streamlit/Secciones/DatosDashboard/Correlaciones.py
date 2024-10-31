##########################################################################################################
# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
#########################################################################################################

df = pd.read_csv("Data/df_renombrado_limpio.csv")

#########################################################################################################
def Desc_Corr():
    st.markdown("<div class='tab-content'>Correlaciones.</div>", unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Matriz de Correlación</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("""
    <p class="big-font">
    Una <strong style='color: violet; font-weight: bold;'>matriz de correlación</strong> es una herramienta estadística que muestra la <strong style='color: violet; font-weight: bold;'>relación entre diferentes variables</strong> en un conjunto de datos. En el contexto de los préstamos, ayuda a identificar cómo <strong style='color: violet; font-weight: bold;'>varían los montos</strong> de los préstamos en relación con otras variables, como la <strong style='color: violet; font-weight: bold;'>duración</strong> del préstamo, la <strong style='color: violet; font-weight: bold;'>tasa de interés</strong>, y más.
    </p>
    <p class="big-font">
    Esta visualización permite a los analistas <strong style='color: violet; font-weight: bold;'>evaluar patrones</strong>, detectar <strong style='color: violet; font-weight: bold;'>anomalías</strong> y tomar decisiones informadas basadas en la <strong style='color: violet; font-weight: bold;'>correlación</strong> entre variables. 
    </p>
    <p class="big-font">
    Cuando una <strong style='color: violet; font-weight: bold;'>variable</strong> se <strong style='color: violet; font-weight: bold;'>correlaciona</strong> más con una u otra, significa que existe una <strong style='color: violet; font-weight: bold;'>relación más fuerte</strong> entre ellas. Por ejemplo, si la <strong style='color: violet; font-weight: bold;'>tasa de interés</strong> está altamente correlacionada con el <strong style='color: violet; font-weight: bold;'>ingreso mensual</strong> de los prestatarios, esto sugiere que a medida que el <strong style='color: violet; font-weight: bold;'>ingreso mensual aumenta</strong>, la <strong style='color: violet; font-weight: bold;'>tasa de interés puede disminuir</strong>, en este caso no se da, pero es un ejemplo para ayudar a entender que significa el <strong style='color: violet; font-weight: bold;'>valor</strong> y las <strong style='color: violet; font-weight: bold;'>correlaciones</strong> de la matriz.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        with st.expander("¿Qué nos aporta esta Matriz de Correlación?", expanded=False):
            st.markdown(""" 
            <p class="big-font">
            La matriz de correlación nos proporciona una <strong style='color: violet; font-weight: bold;'>visión clara</strong> de cómo se relacionan las diferentes <strong style='color: violet; font-weight: bold;'>variables financieras</strong> en el contexto de los préstamos. Nos permite identificar qué <strong style='color: violet; font-weight: bold;'>factores</strong> pueden <strong style='color: violet; font-weight: bold;'>influir</strong> unos con otros, ayudando a los prestamistas a ajustar sus <strong style='color: violet; font-weight: bold;'>ofertas y estrategias</strong>.
            </p>
            <p class="big-font">
            Esta información es crucial para la <strong style='color: violet; font-weight: bold;'>gestión de riesgos</strong> y para una <strong style='color: violet; font-weight: bold;'>visualización rápida</strong> sobre los datos de los préstamos.
            </p>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.expander("¿Para qué sirve esta Matriz de Correlación?", expanded=False):
            st.markdown("""
        <p class="big-font">
        La matriz de correlación permite entender cómo las diferentes <strong style='color: violet; font-weight: bold;'>variables financieras</strong> están relacionadas entre sí. 
        </p>
        <p class="big-font">
        Por ejemplo, puede revelar si existe una correlación positiva entre el <strong style='color: violet; font-weight: bold;'>monto del préstamo</strong> y la <strong style='color: violet; font-weight: bold;'>tasa de interés</strong>, lo que podría indicar que a mayores montos se asignan tasas más altas.
        </p>
        <p class="big-font">
        Esta visualización permite a los analistas identificar <strong style='color: violet; font-weight: bold;'>tendencias</strong> y <strong style='color: violet; font-weight: bold;'>patrones</strong> en el <strong style='color: violet; font-weight: bold;'>comportamiento</strong> de los prestatarios, lo que puede ayudar a <strong style='color: violet; font-weight: bold;'>segmentar clientes</strong> y adaptar ofertas de préstamos a diferentes grupos basándose en sus <strong style='color: violet; font-weight: bold;'>características y necesidades</strong>.
        </p>
        """, unsafe_allow_html=True)

    
    with col3:
        with st.expander("¿Qué utilidad nos da la Matriz de Correlación en este caso?", expanded=False):
            st.markdown("""
        <p class="big-font">
        La matriz de correlación es una herramienta clave en el análisis de datos de préstamos, ya que esta información es invaluable para <strong style='color: violet; font-weight: bold;'>optimizar las ofertas de préstamos</strong>. Al conocer las correlaciones, los prestamistas pueden personalizar sus productos financieros para satisfacer mejor las necesidades de los clientes, lo que a su vez puede aumentar la <strong style='color: violet; font-weight: bold;'>satisfacción del cliente</strong> y la <strong style='color: violet; font-weight: bold;'>retención</strong>.
        </p>
        <p class="big-font">
        Para los <strong style='color: violet; font-weight: bold;'>prestatarios</strong>, entender estas relaciones puede ayudarles a evaluar su <strong style='color: violet; font-weight: bold;'>capacidad de endeudamiento</strong> y como hemos comentado, a tomar mejores decisiones sobre la <strong style='color: violet; font-weight: bold;'>cantidad de dinero</strong> que desean solicitar y el <strong style='color: violet; font-weight: bold;'>tipo de préstamo</strong que les conviene.
        </p>
        <p class="big-font">
        Además, esto fomenta una comunicación más <strong style='color: violet; font-weight: bold;'>clara y efectiva</strong> entre prestamistas y prestatarios, <strong style='color: violet; font-weight: bold;'>mejorando así el proceso de concesión de préstamos</strong>.
        </p>
        """, unsafe_allow_html=True)

                
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown(""" 
    <p class="big-font">
    Puedes seleccionar las variables de interés que quieras relacionar para su visualización.
    </p>
    """, unsafe_allow_html=True)

#########################################################################################################

def Desc_Circular():
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: violet; font-weight: bold; font-size: 3rem; text-align: center'>Visualización mediante Correlación Circular</h2>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("""
    <p class="big-font">
    La <strong style='color: violet; font-weight: bold;'>matriz de correlación circular</strong> es otra forma de visualizar la <strong style='color: violet; font-weight: bold;'>relación entre variables</strong>, permitiendo identificar patrones de manera más intuitiva que una matriz de correlación tradicional. 
    </p>
    <p class="big-font">
    A diferencia de las matrices convencionales, donde las relaciones pueden ser difíciles de interpretar visualmente, la matriz circular permite una <strong style='color: violet; font-weight: bold;'>visualización más clara</strong> de las correlaciones. Las relaciones se representan en un formato radial, lo que facilita la identificación de <strong style='color: violet; font-weight: bold;'>correlaciones fuertes</strong> y <strong style='color: violet; font-weight: bold;'>anomalías</strong> de un vistazo.
    </p>
    <p class="big-font">
    Además, esta representación gráfica ayuda a los analistas a comprender cómo <strong style='color: violet; font-weight: bold;'>se interrelacionan</strong> las variables en un espacio visual reducido, haciendo que la exploración y el análisis de datos sea <strong style='color: violet; font-weight: bold;'>más accesible y eficiente</strong>.
    </p>
    """, unsafe_allow_html=True)

#########################################################################################################
color = "Purples"
def Matriz_corr(df):

    variables = df.select_dtypes(include=[np.number]).columns.tolist()
    if "ID" in variables:
        variables.remove("ID")

    col1, col2 = st.columns([1, 3])
    
    with col1:
        seleccionar_todas = st.checkbox("Seleccionar todas las variables", value=True)

    with col2:
        if seleccionar_todas:
            variables_seleccionadas = variables
        else:
            variables_seleccionadas = st.multiselect("Selecciona variables para la matriz de correlación:", variables)

    if len(variables_seleccionadas) > 1:
        matriz_corr = df[variables_seleccionadas].corr()

        fig = px.imshow(matriz_corr,
                        labels=dict(color="Correlación"),
                        x=matriz_corr.columns,
                        y=matriz_corr.index,
                        color_continuous_scale=color)

        fig.update_layout(width=1000,
                          height=700)

        fig.update_xaxes(tickangle=30)

        st.plotly_chart(fig, use_container_width=True)
        Desc_Circular()
        Correlacion_Circular(df, variables_seleccionadas)
    else:
        st.warning("Por favor, selecciona al menos dos variables.")

#########################################################################################################

def Correlacion_Circular(df, variables_seleccionadas):
    matriz_circular = df[variables_seleccionadas].corr().round(2)

    x, y, correlaciones = zip(*[(col1, col2, matriz_circular.loc[col1, col2])
                                for col1 in matriz_circular.columns
                                for col2 in matriz_circular.columns])

    tamaño_puntos = [abs(c) * 20 for c in correlaciones]

    fig = px.scatter(
        x=x, 
        y=y, 
        size=tamaño_puntos,
        color=correlaciones, 
        color_continuous_scale=color,
        hover_data={"Correlación": correlaciones},
        size_max=15
    )

    fig.update_traces(
        hovertemplate="Relacion entre las Variables: %{x} y %{y}<br>Correlación: %{customdata}<extra></extra>",
        customdata=correlaciones
    )

    fig.update_layout(
        width=700,
        height=700,
        hovermode="closest",
        coloraxis_colorbar=dict(title=None)
    )

    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    fig.update_xaxes(tickangle=30)

    st.plotly_chart(fig, use_container_width=True)

#########################################################################################################