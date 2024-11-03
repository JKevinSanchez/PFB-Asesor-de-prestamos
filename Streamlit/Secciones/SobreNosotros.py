import streamlit as st
from PIL import Image

def SobreNosotros():
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
        .profile-card {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin: 10px;
        }
        .profile-image {
            width: 255px;
            height: auto;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .profile-name {
            font-weight: bold;
            color: violet;
            margin-bottom: 10px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 10px;
        }
        .line-image {
        width: 100%;
        height: 40px;
        object-fit: cover;
        margin-top: 20px;
        margin-bottom: 20px;
        }
        .button {
            margin: 0 5px;
            padding: 10px 15px;
            background-color: violet;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }
        </style>
    """, unsafe_allow_html=True)


    st.markdown("<h1 class='center-font'>Sobre Nosotros</h2>", unsafe_allow_html=True)

    st.markdown("""
        <p class="big-font">
        Aquí puedes conocer a nuestro <strong style='color: violet; font-weight: bold;'>equipo</strong>, esta aplicación es el fruto del trabajo conjunto de todos los integrantes para el <strong style='color: violet; font-weight: bold;'>Proyecto Final de Bootcamp</strong> de <strong style='color: violet; font-weight: bold;'>Hack A Boss</strong>, curso de <strong style='color: violet; font-weight: bold;'>Data Science & IA</strong>
        </p>
        <p class="big-font">
        Tienes a tu disposición nuestros perfiles de <strong style='color: violet; font-weight: bold;'>LinkedIn & GitHub</strong> para que puedas investigar sobre cómo nos ha ido en un futuro y qué metas hemos alcanzado, además de acceder a nuestro trabajo directamente.
        </p>                
        <p class="big-font">
        <strong style='color: violet; font-weight: bold;'>Te damos las gracias</strong> por visitar y utilizar nuestra aplicación de <strong style='color: violet; font-weight: bold;'>Asesores de Préstamos</strong>, esperamos que haya sido de tu agrado y hayas quedado satisfecho/a con el trabajo realizado por los alumnos e integrantes de este equipo:
        </p>
        """, unsafe_allow_html=True)

    st.markdown("<img src='https://i.ibb.co/7NM1Ln7/9150117.jpg' class='line-image'/>", unsafe_allow_html=True)

    col0, col1, col2, col00 = st.columns((1, 1, 1, 1))
    
    col0, col1, col2, col00 = st.columns((1, 1, 1, 1))
    
    with col1:
        st.markdown("""
            <p class="big-font">
            <strong style='color: violet; font-weight: bold;'>César Rabadán Cuevas</strong>
            </p>
            """, unsafe_allow_html=True)

        Cesar = Image.open("Data/Imagenes/Cesar.png")
        Cesar = Cesar.convert("RGB")
        Cesar = Cesar.resize((300, 300))
        st.image(Cesar)

        col3, col4 = st.columns(( 1, 1))
        col3.link_button("Linkedin", "www.linkedin.com/in/cesarrabadancuevas")
        col4.link_button("GitHub", "https://github.com/CesarRabadan")

    with col1:
        st.markdown("""
            <p class="big-font">
            <strong style='color: violet; font-weight: bold;'>Amanda Herranz Perlova</strong>
            </p>
            """, unsafe_allow_html=True)

        Amanda = Image.open("Data/Imagenes/Amanda.png")
        Amanda = Amanda.convert("RGB")
        Amanda = Amanda.resize((300, 300))
        st.image(Amanda)

        col3, col4 = st.columns(( 1, 1))
        col3.link_button("Linkedin", "https://www.linkedin.com/in/amandaherranzperlova/")
        col4.link_button("GitHub", "https://github.com/amyperlova")

    with col2:
        st.markdown("""
            <p class="big-font">
            <strong style='color: violet; font-weight: bold;'>Paula Lobato Blanco</strong>
            </p>
            """, unsafe_allow_html=True)

        Paula = Image.open("Data/Imagenes/Paula.png")
        Paula = Paula.convert("RGB")
        Paula = Paula.resize((300, 300))
        st.image(Paula)

        col3, col4 = st.columns(( 1, 1))
        col3.link_button("Linkedin", "https://www.linkedin.com/in/paulalobatoblanco")
        col4.link_button("GitHub", "https://github.com/Paaulalobato")

    with col2:
        st.markdown("""
            <p class="big-font">
            <strong style='color: violet; font-weight: bold;'>Jacques Kevin Sánchez Guerra</strong>
            </p>
            """, unsafe_allow_html=True)

        Kevin = Image.open("Data/Imagenes/Kevin.png")
        Kevin = Kevin.convert("RGB")
        Kevin = Kevin.resize((300, 300))
        st.image(Kevin)

        col3, col4 = st.columns(( 1, 1))
        col3.link_button("Linkedin", "https://www.linkedin.com/in/jacqueskevin/")
        col4.link_button("GitHub", "https://github.com/JKevinSanchez")

    st.markdown("<img src='https://i.ibb.co/7NM1Ln7/9150117.jpg' class='line-image'/>", unsafe_allow_html=True)

if __name__ == "__main__":
    SobreNosotros()