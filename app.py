import streamlit as st
from asp_motor import calcular_variables

st.title("Software de Riego por Aspersión 💧")

etp = st.number_input("ETp (mm/día)", value=5.8)
eficiencia = st.number_input("Eficiencia (0-1)", value=0.75)
q = st.number_input("Caudal disponible (L/s)", value=0.5)
sup = st.number_input("Superficie de riego (ha)", value=0.26)

if st.button("Calcular"):
    res = calcular_variables(etp, eficiencia, q, sup)
    st.success("Resultados")
    for k, v in res.items():
        st.write(f"**{k}**: {v:.3f}")
