import streamlit as st

def Introduccion():
    st.markdown("""
        <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .center-font {
            font-size: 20px;
            text-align: center;
            color: var(--primary-text-color);
        }
        .big-font {
            font-size: 17px;
            color: var(--primary-text-color);
            text-align: left;
        }
        .sub-font {
            font-size: 22px;
            color: #FAA227;
            font-weight: bold;
        }
        .highlight {
            color: violet;
            font-weight: bold;
        }
        .line-image {
            width: 100%;
            height: 60px;
            object-fit: cover;
            margin-top: 20px;
        }
        .divider {
        border: none;
        height: 2px;
        background-color: violet;
        margin: 0px 0;
        }
        </style>
    """, unsafe_allow_html=True)

##########################################################################################################
# Titulo de la pagina
    st.markdown("<h1 style='text-align: center; color: violet; font-size: 3em;'>Introducción a nuestro Asesor de Préstamos</h1>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

##########################################################################################################
# Introduccion a la aplicacion
    col_1, col_2, col_3 = st.columns((0.2, 1, 0.2))

    col_2.markdown(
        "<p class='big-font'>"
        "Bienvenido/a a nuestro <span class='highlight'>Proyecto Final de Bootcamp de Data Science & IA</span>.<br><br>"
        
        "Esta aplicación consiste en un <span class='highlight'>Asesor de Préstamos</span> que nos permite analizar datos de préstamos y evaluar su viabilidad. Esto puede ser de gran utilidad para entender mejor las dinámicas de los préstamos y las variables que influyen a la hora de estudiar la capacidad de pago de los prestatarios.<br><br>"
        
        "Gracias a un gran y exhaustivo análisis de datos de préstamos aceptados y rechazados, hemos podido crear un <span class='highlight'>Modelo Predictivo</span> para el objetivo comentado anteriormente sobre la capacidad de pago.<br><br>"
        
        "Nuestra aplicación se divide en diferentes secciones encontradas a la izquierda, en la pestaña de <span class='highlight'>Navegación</span>, aquí podéis encontrar:<br><br>"
        
        "- <span class='highlight'>Introducción</span>: Es la página principal, que estás visualizando actualmente, con una explicación del trabajo y una breve introducción a la aplicación.<br><br>"
        
        "- <span class='highlight'>Dashboard</span>: Aquí encontrarás una sección de visualización basada en datos de préstamos, lo cual te permitirá investigar, entender y comprobar diferentes datos o variables y cómo se relacionan entre sí.<br><br>"
        
        "- <span class='highlight'>Variables y Modelo Utilizado</span>: Aquí conocerás más a fondo qué variables son las más importantes para predecir si un préstamo es viable o no y el modelo de Machine Learning que hemos utilizado, para que te familiarices con nuestro trabajo.<br><br>"

        "- <span class='highlight'>Asesor</span>: En esta pestaña se encuentra el modelo predictivo que hemos comentado. Aquí podrás, mediante la introducción de ciertos datos que se piden, analizar el préstamo que se pretende conceder o estudiar, para evaluarlo y hacer la predicción de su capacidad de ser pagado.<br><br>"

        "- <span class='highlight'>Metodología, Resultados y Conclusiones</span>: En esta sección, dispondrás de nuestra metodología de trabajo utilizada para sacar adelante la aplicación, nuestros resultados, basándose en una explicación y análisis del modelo predictivo utilizado y nuestras conclusiones sobre los resultados del proyecto.<br><br>"
        
        "- <span class='highlight'>Sobre Nosotros</span>: Y por último, podrás ponernos cara, conocernos más si tienes interés en contactar con nosotros y vistar nuestras redes profesionales.<br><br>"

        "<span class='highlight'>Ahora le animamos a explorar nuestra aplicación y descubrir el fruto de nuestro trabajo, ¡muchas gracias!.</span>"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("<img src='https://i.ibb.co/7NM1Ln7/9150117.jpg' class='line-image'/>", unsafe_allow_html=True)

if __name__ == "__main__":
    Introduccion()

