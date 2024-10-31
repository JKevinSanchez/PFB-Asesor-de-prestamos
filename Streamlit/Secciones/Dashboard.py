##########################################################################################################
# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
##########################################################################################################
#Funciones
from Secciones.DatosDashboard.Analisis import *
from Secciones.DatosDashboard.Visualizaciones import *
from Secciones.DatosDashboard.Correlaciones import *
from Secciones.DatosDashboard.Conclusiones import *
##########################################################################################################


def Dashboard():
    st.markdown("""
        <style>
        .big-font {
            font-size: 20px;
            color: #FFFFFF;
            text-align: left;
        }
        .sub-font {
            font-size: 25px;
            color: violet;
            font-weight: bold;                    
        }
        .center-font {
            font-size: 40px;
            color: violet;
            text-align: center;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px;  
            justify-content: center;  
            display: flex;
            background-image: url('https://i.ibb.co/7NM1Ln7/9150117.jpg');
            background-size: cover;
            background-position: center calc(100% - 630px);
            border-radius: 5px;
            padding: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 60px;
            width: auto;
            white-space: pre-wrap;
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 3px 3px 0px 0px;
            gap: 1px;
            padding: 40px 90px;
            font-size: 1rem;
            color: #FFFFFF;
            font-weight: bold;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stTabs [aria-selected="true"] {
            background-color: rgba(255, 255, 255, 0.5);
        }
        .tab-content {
            background-image: url('https://i.ibb.co/7NM1Ln7/9150117.jpg');
            background-size: cover;
            background-position: center calc(100% - 430px);
            border-radius: 5px;
            padding: 20px;
            margin-top: 20px;
            color: #FFFFFF;
            font-weight: bold;
            text-align: center;
            font-size: 2rem;
        }
        .divider {
            border: none;
            height: 2px;
            background-color: violet;
            margin: 0px 0;
        }
        .text-column {
            text-align: left;
        }
        .line-image {
        width: 100%;
        height: 60px;
        object-fit: cover;
        margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    ##########################################################################################################  
    #Introduccion
    st.markdown("<h1 class='center-font'>Análisis de Préstamos</h2>", unsafe_allow_html=True)

    st.markdown("""
        <p class="big-font">
        La <strong style='color: violet; font-weight: bold;'>financiación</strong> es una parte crucial de la economía, y entender los factores que influyen en la concesión de préstamos puede ser la clave para una mejor <strong style='color: violet; font-weight: bold;'>toma de decisiones</strong> financieras.
        </p>
        <p class="big-font">
        Este <strong style='color: violet; font-weight: bold;'>dashboard interactivo</strong> te permitirá explorar los datos de préstamos y obtener información valiosa sobre cómo funcionan sus diferentes variables y cómo se relacionan entre sí.
        </p>                
        <p class="big-font">
        Hemos recopilado y analizado <strong style='color: violet; font-weight: bold;'>datos relevantes</strong> sobre <strong style='color: violet; font-weight: bold;'>préstamos aceptados y rechazados</strong> para brindarte una visión completa mediante <strong style='color: violet; font-weight: bold;'>gráficas</strong> y <strong style='color: violet; font-weight: bold;'>explicaciones</strong>. A continuación, encontrarás nuestras <strong style='color: violet; font-weight: bold;'>visualizaciones</strong> que te ayudarán a entender las <strong style='color: violet; font-weight: bold;'>dinámicas de los préstamos</strong>.
        </p>
        """, unsafe_allow_html=True)

    ########################################################################################################## 
    # Partes o tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Análisis de Datos",
                                       "Visualizaciones",
                                       "Correlaciones",
                                       "Conclusiones"])
    
    # Contenido de cada tab
    with tab1:
        Desc_Analisis()
        Datos_Analisis()
        
##########################################################################################################
    with tab2:
        Desc_BoxViolin()            
   
        Desc_Histograma()
        columna_seleccionada = ()
        Histograma(df, columna_seleccionada)
        Grafico_Dispersion_3D(df) 

##########################################################################################################
    with tab3:
        Desc_Corr()
        Matriz_corr(df)

##########################################################################################################
    with tab4:
       Conclusiones()

##########################################################################################################
    st.markdown("<img src='https://i.ibb.co/7NM1Ln7/9150117.jpg' class='line-image'/>", unsafe_allow_html=True)
if __name__ == "__main__":
    Dashboard()