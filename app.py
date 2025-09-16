# app.py
import streamlit as st
from riego import calcular_riego

st.set_page_config(page_title="Diseño de Riego por Aspersión", layout="wide")

st.title("💧 Diseño de Riego por Aspersión")

st.sidebar.header("Parámetros de Entrada")

# Inputs desde el usuario
etp = st.sidebar.number_input("ETP (mm/día)", value=5.0, step=0.1)
kc = st.sidebar.number_input("Coeficiente de cultivo (Kc)", value=1.0, step=0.05)
eficiencia = st.sidebar.slider("Eficiencia del sistema (%)", 50, 95, 75) / 100
superficie = st.sidebar.number_input("Superficie a regar (ha)", value=1.0, step=0.1)
q_disp = st.sidebar.number_input("Caudal disponible (L/s)", value=2.0, step=0.1)
sep = st.sidebar.number_input("Separación entre aspersores (m)", value=12, step=1)
q_asp = st.sidebar.number_input("Caudal de aspersor (L/s)", value=0.8, step=0.1)
long_tub = st.sidebar.number_input("Longitud tubería (m)", value=100, step=1)
diam = st.sidebar.number_input("Diámetro tubería (mm)", value=63, step=1)
c_hw = st.sidebar.number_input("Coef. Hazen-Williams", value=150, step=1)

# Calcular resultados
if st.sidebar.button("Calcular"):
    resultados = calcular_riego(
        etp_mm_dia=etp, kc=kc, eficiencia=eficiencia, superficie_ha=superficie,
        q_disp_ls=q_disp, separacion_m=sep, q_asp_ls=q_asp,
        long_tuberia_m=long_tub, diametro_mm=diam, C_HW=c_hw
    )

    st.subheader("📊 Resultados del diseño")
    for k, v in resultados.items():
        st.write(f"**{k}**: {v:.3f}")
