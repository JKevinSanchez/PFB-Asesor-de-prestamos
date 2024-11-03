import streamlit as st

from Secciones.DatosMetodologia.DatosMetodologia import *


def Metodologia():
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
            margin-top: 0px;
            margin-bottom: 0px;
            color: #FFFFFF;
            font-weight: bold;
            text-align: center;
            font-size: 2rem;
        }
        .divider {
            border: none;
            height: 2px;
            margin-bottom: 0px;
            background-color: violet;
            margin: 0px 0;
        }
        .text-column {
            text-align: left;
        }
        .vertical-separator {
            display: inline-block;
            width: 2px;
            background-color: violet;
            height: 350px;
            margin: 0 20px;
        }
        .line-image {
        width: 100%;
        height: 60px;
        object-fit: cover;
        margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["Metodología",
                                "Resultados",
                                "Conclusiones"])
    with tab1:
        Metod()
    with tab2:
        Resultados()
    with tab3:
        Conclusiones()

    st.markdown("<img src='https://i.ibb.co/7NM1Ln7/9150117.jpg' class='line-image'/>", unsafe_allow_html=True)
if __name__ == "__main__":
    Metodologia()