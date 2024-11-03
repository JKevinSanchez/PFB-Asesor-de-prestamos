##########################################################################################################
#Librerias
import streamlit as st
from streamlit_option_menu import option_menu
##########################################################################################################
#Funciones Pagina
from config_pagina import CONFIG
from Secciones.Introduccion import Introduccion
from Secciones.Dashboard import Dashboard
from Secciones.Asesor import Asesor
from Secciones.VariablesModelo import Var_Modelo
from Secciones.Metodologia import Metodologia
from Secciones.SobreNosotros import SobreNosotros
##########################################################################################################

# Configuracion de la aplicación
st.set_page_config(**CONFIG)

##########################################################################################################
# Estilo de nuestra app
estilo = """
<style>
[data-testid="stAppViewBlockContainer"] {
    background-image: url("https://img.freepik.com/vector-gratis/borde-onda-sintetica-neon-vector-plantilla-cartel-purpura-oscuro_53876-165947.jpg?t=st=1729530215~exp=1729533815~hmac=8a8176b9ee771d46b0f319f7233523ccf7c63654c9f4989ef27cb4efba249e81&w=740");
    background-size: cover;
    background-color: #111111;
    padding-left: 150px;
    padding-right: 150px;
}

[data-testid="stHeader"] {
    background-image: url("https://i.ibb.co/7NM1Ln7/9150117.jpg");
    background-size: cover;
    background-position: center calc(100% - 1030px);
}

.nav-link:hover {
    background-color: #444444;
    color: white;
}
</style>
"""

st.markdown(estilo, unsafe_allow_html=True)

##########################################################################################################
# Ponemos el Menú en la parte superior para una visualización más limpia
def pagina_principal():
    selected_option = option_menu(
        menu_title=None,
        options=["Introducción", "Dashboard", "Variables y Modelo Utilizado", "Asesor", "Metodología", "Sobre Nosotros"],
        icons=["house", "bar-chart", "book", "person", "play", "question"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "center",
                "margin": "0px",
                "padding": "8px",
                "color": "white",
                "background-color": "transparent",
            },
            "nav-link-selected": {"background-color": "violet", "color": "white"},
        }
    )

    if selected_option == "Introducción":
        Introduccion()
    elif selected_option == "Dashboard":
        Dashboard()
    elif selected_option == "Variables y Modelo Utilizado":
        Var_Modelo()
    elif selected_option == "Asesor":
        Asesor()
    elif selected_option == "Metodología":
        Metodologia()
    elif selected_option == "Sobre Nosotros":
        SobreNosotros()

if __name__ == "__main__":
    pagina_principal()