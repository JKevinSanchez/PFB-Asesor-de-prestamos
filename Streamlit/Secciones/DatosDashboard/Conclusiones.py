##########################################################################################################
# Librerias
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.express as px
#########################################################################################################

df = pd.read_csv("Data/df_renombrado_limpio.csv")

#########################################################################################################

def Conclusiones():
    st.markdown("<div class='tab-content'>Conclusiones.</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    
    st.markdown("""
    <p class="big-font">
    Aquí vamos a repasar las <strong style='color: violet; font-weight: bold;'>Conclusiones</strong> obtenidas a partir del <strong style='color: violet; font-weight: bold;'>análisis de datos de préstamos</strong>, en el que hemos explorado las relaciones más significativas entre las variables.
    </p>
    <p class="big-font">
    Las conclusiones generales de este análisis indican que una comprensión profunda de las <strong style='color: violet; font-weight: bold;'>interacciones entre variables</strong> es esencial para una <strong style='color: violet; font-weight: bold;'>gestión efectiva del riesgo</strong> y la <strong style='color: violet; font-weight: bold;'>toma de decisiones</strong> en el ámbito de los préstamos. Esta información <strong style='color: violet; font-weight: bold;'>no solo beneficia a los prestamistas</strong>, sino que también proporciona a los prestatarios una <strong style='color: violet; font-weight: bold;'>mejor perspectiva</strong> sobre cómo sus características pueden <strong style='color: violet; font-weight: bold;'>influir</strong> en las <strong style='color: violet; font-weight: bold;'>condiciones</strong> de su préstamo.
    </p>
    <p class="big-font">
    En resumen, el <strong style='color: violet; font-weight: bold;'>análisis de datos</strong>, las <strong style='color: violet; font-weight: bold;'>visualizaciones</strong> presentadas y las <strong style='color: violet; font-weight: bold;'>correlaciones</strong> entre variables, ofrecen una <strong style='color: violet; font-weight: bold;'>base sólida</strong> para entender <strong style='color: violet; font-weight: bold;'>cómo</strong> se <strong style='color: violet; font-weight: bold;'>distribuyen</strong> y <strong style='color: violet; font-weight: bold;'>manejan</strong> los préstamos, permitiendo a todos los involucrados en el proceso, conocer mejor el <strong style='color: violet; font-weight: bold;'>ámbito de los préstamos</strong> y sus <strong style='color: violet; font-weight: bold;'>características</strong>.
    </p>
    """, unsafe_allow_html=True)

#########################################################################################################
