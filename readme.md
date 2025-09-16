# Software de Riego por Aspersión 💧

Este paquete convierte cálculos básicos de riego por aspersión en un software Python.

## Estructura

- `asp_motor.py`: Motor matemático (fórmulas).
- `cli.py`: Interfaz de línea de comandos.
- `app.py`: Interfaz gráfica con Streamlit.
- `reportes.py`: Exportar resultados a PDF y CSV.
- `requirements.txt`: Librerías necesarias.
- `README.md`: Esta guía.

## Uso local

```bash
pip install -r requirements.txt
python cli.py --etp 5.8 --eficiencia 0.75 --q 0.5 --sup 0.26
streamlit run app.py
