import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Función para calcular factor de certidumbre según heurísticas
def calcular_cf(row):
    cf = 1.0
    if row['distancia'] > 0.9:
        cf *= 0.6
    elif row['distancia'] > 0.7:
        cf *= 0.8

    if row['shotType'] == 3:
        cf *= 0.7
    elif row['shotType'] >= 4:
        cf *= 0.5
    else:
        cf *= 0.9
    return round(cf, 2)

# Construcción del sistema difuso
def crear_sistema_difuso():
    distancia = ctrl.Antecedent(np.arange(0, 1.2, 0.01), 'distancia')
    angulo = ctrl.Antecedent(np.arange(0, 0.7, 0.01), 'angulo')
    remate = ctrl.Antecedent(np.arange(1, 5, 1), 'remate')
    xg = ctrl.Consequent(np.arange(0, 1.05, 0.05), 'xg')

    distancia['corta'] = fuzz.trimf(distancia.universe, [0, 0, 0.4])
    distancia['media'] = fuzz.trimf(distancia.universe, [0.3, 0.6, 0.9])
    distancia['larga'] = fuzz.trimf(distancia.universe, [0.8, 1.1, 1.1])

    angulo['cerrado'] = fuzz.trimf(angulo.universe, [0, 0, 0.2])
    angulo['medio'] = fuzz.trimf(angulo.universe, [0.1, 0.3, 0.5])
    angulo['abierto'] = fuzz.trimf(angulo.universe, [0.4, 0.6, 0.6])

    remate['pie'] = fuzz.trimf(remate.universe, [1, 1, 2])
    remate['cabeza'] = fuzz.trimf(remate.universe, [2.5, 3, 3.5])
    remate['otro'] = fuzz.trimf(remate.universe, [3.5, 4, 4])

    xg['bajo'] = fuzz.trimf(xg.universe, [0, 0, 0.4])
    xg['medio'] = fuzz.trimf(xg.universe, [0.3, 0.5, 0.7])
    xg['alto'] = fuzz.trimf(xg.universe, [0.6, 1, 1])

    reglas = [
        ctrl.Rule(distancia['corta'] & angulo['abierto'] & remate['pie'], xg['alto']),
        ctrl.Rule(distancia['corta'] & angulo['medio'] & remate['pie'], xg['medio']),
        ctrl.Rule(distancia['media'] & angulo['medio'] & remate['cabeza'], xg['medio']),
        ctrl.Rule(distancia['larga'] | angulo['cerrado'] | remate['otro'], xg['bajo']),
    ]

    sistema_ctrl = ctrl.ControlSystem(reglas)
    return ctrl.ControlSystemSimulation(sistema_ctrl)

# Función para calcular distancia y ángulo
def calcular_distancia(x, y):
    return np.sqrt((1 - x)**2 + (0.5 - y)**2)

def calcular_angulo(x, y):
    left_post = np.sqrt((1 - x)**2 + (0.44 - y)**2)
    right_post = np.sqrt((1 - x)**2 + (0.56 - y)**2)
    goal_width = 0.12
    angle = np.arctan2(goal_width, left_post + right_post)
    return angle

# Función principal que recibe un DataFrame con tiros y calcula xG ajustado
def calcular_xg_difuso(df):
    df = df.copy()
    df['distancia'] = calcular_distancia(df['X'], df['Y'])
    df['angulo'] = calcular_angulo(df['X'], df['Y'])
    df['cf'] = df.apply(calcular_cf, axis=1)

    resultados = []

    for _, fila in df.iterrows():
        sistema = crear_sistema_difuso()  # Reinicia el sistema para cada fila
        sistema.input['distancia'] = fila['distancia']
        sistema.input['angulo'] = fila['angulo']
        sistema.input['remate'] = fila['shotType']

        try:
            sistema.compute()
            xg_difuso = sistema.output['xg']
        except:
            xg_difuso = None

        if xg_difuso is not None:
            xg_ajustado = round(xg_difuso * fila['cf'], 4)
        else:
            xg_ajustado = None

        resultados.append({
            'distancia': round(fila['distancia'], 3),
            'angulo': round(fila['angulo'], 3),
            'shotType': fila['shotType'],
            'cf': fila['cf'],
            'xG_difuso': round(xg_difuso, 4) if xg_difuso is not None else None,
            'xG_ajustado': xg_ajustado,
            'xG_real': round(fila['xG'], 4) if 'xG' in fila else None
        })

    return pd.DataFrame(resultados)

if __name__ == "__main__":
    opcion = input("¿Quieres usar los datos de ejemplo o cargar un archivo CSV? (ejemplo/csv): ").strip().lower()

    if opcion == "csv":
        ruta = input("Ingresa la ruta del archivo CSV: ").strip()
        try:
            df = pd.read_csv(ruta)
            df.columns = df.columns.str.strip()
            print("Archivo cargado correctamente y columnas limpiadas.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            exit(1)
    else:
        example_data = {
            'X': [0.85, 0.7, 0.95],
            'Y': [0.5, 0.3, 0.55],
            'shotType': [1, 3, 2],  # pie derecho, cabeza, pie izquierdo
            'xG': [0.6, 0.3, 0.7]   # valores reales de xG, para comparar
        }
        df = pd.DataFrame(example_data)
        print("Usando datos de ejemplo.")

    resultados = calcular_xg_difuso(df)
    print(resultados)
