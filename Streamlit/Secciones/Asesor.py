##########################################################################################################
# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
##########################################################################################################
#Funciones
from Secciones.DatosAsesor.datosAsesor import *
##########################################################################################################

def Asesor():
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
    st.markdown("<h1 class='center-font'>Asesor de Préstamos</h1>", unsafe_allow_html=True)

    st.markdown("""
    <p class="big-font">
    Este es el resultado de nuestro trabajo de <strong style='color: violet; font-weight: bold;'>Data Science & IA</strong>, nuestro modelo de <strong style='color: violet; font-weight: bold;'>Machine Learning</strong>. Aquí descubrirás, dependiendo de los <strong style='color: violet; font-weight: bold;'>datos que introduzcas</strong>, si un préstamo va a ser viable o no.
    </p>
    <p class="big-font">            
    Además, también verás en qué se basa, gracias a los <strong style='color: violet; font-weight: bold;'>datos</strong> que pedimos y las <strong style='color: violet; font-weight: bold;'>explicaciones</strong> que te proporcionamos, sabrás qué se tiene en cuenta para nuestro <strong style='color: violet; font-weight: bold;'>Modelo Predictivo</strong>.
    </p>            
    <p class="big-font">            
    Nuestra <strong style='color: violet; font-weight: bold;'>herramienta</strong>, que verás a continuación, utiliza el modelo de <strong style='color: violet; font-weight: bold;'>Machine Learning</strong> que hemos comentado. <strong style='color: violet; font-weight: bold;'>
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align: center; font-size: 30px; color: white; font-weight: bold;">
    ¡Adelante, siéntete libre de probarlo!
    </p>
    """, unsafe_allow_html=True)
    
##########################################################################################################
    Evaluacion()
    st.markdown("<img src='https://i.ibb.co/7NM1Ln7/9150117.jpg' class='line-image'/>", unsafe_allow_html=True)