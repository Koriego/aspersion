import math

def calcular_riego(etp_mm_dia, kc, eficiencia, superficie_ha,
                   q_disp_ls, separacion_m, q_asp_ls,
                   long_tuberia_m, diametro_mm, C_HW=150):
    """Cálculos principales de riego por aspersión"""

    # 1. Evapotranspiración de cultivo
    etc = etp_mm_dia * kc

    # 2. Demanda neta y bruta
    demanda_neta_mm = etc
    demanda_bruta_mm = demanda_neta_mm / eficiencia

    # 3. Demanda en L/s·ha
    lps_por_mm = 0.01157  # coef. conversión mm/día → L/s·ha
    demanda_lps_ha = demanda_bruta_mm * lps_por_mm

    # 4. Superficie potencial con el caudal disponible
    sup_potencial_ha = q_disp_ls / demanda_lps_ha

    # 5. Número de aspersores
    area_asp_m2 = separacion_m * separacion_m
    sup_m2 = superficie_ha * 10000
    n_aspersores = sup_m2 / area_asp_m2

    # 6. Caudal total requerido
    q_total_ls = q_asp_ls * n_aspersores

    # 7. Tiempo de riego por turno (h)
    volumen_L = demanda_bruta_mm * sup_m2  # 1 mm = 1 L/m2
    tiempo_h = volumen_L / (q_disp_ls * 3600)

    # 8. Pérdidas por Hazen–Williams
    q_m3s = q_total_ls / 1000
    d_m = diametro_mm / 1000
    hf = 10.67 * long_tuberia_m * (q_m3s**1.852) / ((C_HW**1.852) * (d_m**4.87))

    return {
        "ETc_mm_dia": etc,
        "Demanda_neta_mm": demanda_neta_mm,
        "Demanda_bruta_mm": demanda_bruta_mm,
        "Demanda_Ls_ha": demanda_lps_ha,
        "Superficie_potencial_ha": sup_potencial_ha,
        "N_aspersores": n_aspersores,
        "Q_total_Ls": q_total_ls,
        "Tiempo_riego_h": tiempo_h,
        "hf_m": hf,
    }

# Ejemplo de uso:
if __name__ == "__main__":
    res = calcular_riego(
        etp_mm_dia=5.8, kc=1.1, eficiencia=0.75, superficie_ha=0.5,
        q_disp_ls=2.5, separacion_m=12, q_asp_ls=0.8,
        long_tuberia_m=100, diametro_mm=63
    )
    for k, v in res.items():
        print(f"{k}: {v:.3f}")
