def calcular_variables(etp_mm_dia, eficiencia, q_disponible_ls, sup_riego_ha):
    """Motor de cálculo de riego por aspersión"""
    # Demanda neta
    demanda_mm_dia = etp_mm_dia / eficiencia

    # Conversión: 1 mm/día ≈ 0.01157 L/s/ha
    lps_por_mm = 0.01157
    demanda_lps_ha = demanda_mm_dia * lps_por_mm

    # Superficie potencial
    sup_potencial = q_disponible_ls / demanda_lps_ha

    return {
        "Demanda (mm/día)": demanda_mm_dia,
        "Demanda (L/s/ha)": demanda_lps_ha,
        "Superficie potencial (ha)": sup_potencial,
        "Superficie real (ha)": sup_riego_ha,
    }
