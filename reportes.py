import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def exportar_resultados(res, nombre="reporte.pdf"):
    """Exporta resultados en PDF"""
    doc = SimpleDocTemplate(nombre)
    styles = getSampleStyleSheet()
    flow = [Paragraph("Reporte de Riego por Aspersión", styles["Title"])]
    flow.append(Spacer(1, 20))
    for k, v in res.items():
        flow.append(Paragraph(f"{k}: {v:.3f}", styles["Normal"]))
    doc.build(flow)

def exportar_csv(res, nombre="reporte.csv"):
    """Exporta resultados en CSV"""
    df = pd.DataFrame([res])
    df.to_csv(nombre, index=False)
