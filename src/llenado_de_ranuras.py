import networkx as nx
import matplotlib.pyplot as plt
import datetime
import re
#from colorama import init, Fore, Back, Style

from lib.diseno import Colores

def semantic_network_animals():
   G = nx.DiGraph()
   animals = {
      "Perro": [("mamífero", "reproducción"), ("terrestre", "entorno")],
      "Gato": [("mamífero", "reproducción"), ("terrestre", "entorno")],
      "Ornitorrinco": [("mamífero", "reproducción"), ("ovíparo", "reproducción"), ("acuático", "entorno")],
      "Murciélago": [("mamífero", "reproducción"), ("aéreo", "entorno")],
      "Gallina": [("ovíparo", "reproducción"), ("terrestre", "entorno")],
      "Águila": [("ovíparo", "reproducción"), ("aéreo", "entorno")],
      "Pingüino": [("ovíparo", "reproducción"), ("acuático", "entorno"), ("terrestre", "entorno")],
      "Delfín": [("mamífero", "reproducción"), ("acuático", "entorno")],
      "Tiburón": [("ovíparo", "reproducción"), ("acuático", "entorno")],
      "Rana": [("ovíparo", "reproducción"), ("acuático", "entorno"), ("terrestre", "entorno")]
   }

   # Caragar los nodos y las aristas en el grafo
   for animal, relations in animals.items():
      G.add_node(animal)
      for characteristic, relation_type in relations:
         G.add_node(characteristic)
         G.add_edge(animal, characteristic, label=relation_type)

   # Función para obtener animales por característica
   def get_animals_by_characteristic(characteristic):
      return [node for node in G.predecessors(characteristic)]
   
   # Características a consultar
   characteristics_to_query = ["mamífero", "ovíparo", "acuático", "terrestre", "aéreo"]

   # Mostrar resultados
   for characteristic in characteristics_to_query:
      found_animals = get_animals_by_characteristic(characteristic)
      print(f"Animales con la característica '{Colores.AMARILLO + characteristic + Colores.AMARILLO_CLARO}': {found_animals}{Colores.DEFAULT}")
   # Dibujar el grafo
   pos = nx.spring_layout(G, seed=55)  # Posiciones para todos los nodos
   plt.figure(figsize=(12, 8))
   nx.draw_networkx_nodes(G, pos, node_color='lightyellow', node_size=1500)
   nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
   nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
   # Obtener etiquetas de las aristas
   edge_labels = nx.get_edge_attributes(G, 'label')
   nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkgreen', font_size=8)
   plt.title("Red Semántica de Animales con Relaciones Etiquetadas")
   plt.axis('off')
   plt.show()

def frames_medical_diagnostics():
   # Definición de frames
   frames = {
      "Diabetes": {"piel": "seca", "orina": "frecuente", "energia": "baja", "ojos": "visión borrosa", "cabello": "normal"},
      "Hipotiroidismo": {"piel": "seca", "orina": "normal", "energia": "baja", "ojos": "hinchados", "cabello": "quebradizo"},
      "Anemia": {"piel": "pálida", "orina": "normal", "energia": "muy baja", "ojos": "normales", "cabello": "normal"},
      "Insuficiencia renal": {"piel": "amarillenta", "orina": "oscura", "energia": "baja", "ojos": "hinchados", "cabello": "normal"},
      "Hipertiroidismo": {"piel": "húmeda", "orina": "frecuente", "energia": "alta", "ojos": "saltones", "cabello": "fino"},
      "Deshidratación": {"piel": "seca", "orina": "oscura", "energia": "baja", "ojos": "hundidos", "cabello": "normal"},
      "Hepatitis": {"piel": "amarillenta", "orina": "oscura", "energia": "baja", "ojos": "amarillentos", "cabello": "normal"},
      "Lupus": {"piel": "erupciones", "orina": "espumosa", "energia": "baja", "ojos": "secos", "cabello": "caída"}
   }

   # Perfiles de pacientes
   pacientes = {
      "Paciente 1": {"piel": "seca", "orina": "frecuente", "energia": "baja", "ojos": "visión borrosa", "cabello": "normal"},
      "Paciente 2": {"piel": "pálida", "orina": "normal", "energia": "muy baja", "ojos": "normales", "cabello": "normal"},
      "Paciente 3": {"piel": "amarillenta", "orina": "oscura", "energia": "baja", "ojos": "amarillentos", "cabello": "normal"},
      "Paciente 4": {"piel": "erupciones", "orina": "espumosa", "energia": "baja", "ojos": "secos", "cabello": "caída"}
   }

   # Obtencion del diagnostico
   for nombre, sintomas in pacientes.items():
      coincidencias = {}
      for enfermedad, caracteristicas in frames.items():
         match = sum(1 for k in sintomas if sintomas[k] == caracteristicas.get(k))
         coincidencias[enfermedad] = match
      diagnostico = max(coincidencias, key=coincidencias.get)
      print(f"{nombre}: Diagnóstico sugerido -> {Colores.MAGENTA_CLARO + diagnostico + Colores.DEFAULT}")
   print()

def conceptual_dependency():
   # Diccionario de acciones primitivas y sus verbos asociados
   acciones_primitivas = {
      'ATRANS': ['dio', 'entregó', 'pasó', 'regaló', 'prestó', "llevó"],         # Transferencia abstracta
      'MTRANS': ['dijo', 'informó', 'comentó', 'contó', 'habló', 'mencionó'],    # Transferencia mental
      'PROPEL': ['empujó', 'lanzó', 'golpeó'],                                   # Aplicación de fuerza
      'GRASP': ['tomó', 'agarró', 'cogió']
   }
   # Lista de oraciones a analizar
   oraciones = [
      "Aaron le dio un libro a Juan",
      "Juan le dijo un secreto a Mauricio",
      "Cesar le entregó un regalo y un pastel a Brandon",
      "Brandon golpeó a Jairo",
      "Cesar dijo a Marvin que lo llamara",
      "Mauricio empujó a Jairo",
      "Jairo tomó un libro de Aaron",
      "Aaron le regaló un coche a Juan"
   ]

   # Función para identificar la acción primitiva en una oración
   def identificar_accion(oracion):
      for accion, verbos in acciones_primitivas.items():
         for verbo in verbos:
            if verbo in oracion:
                  return accion, verbo
      return None, None
   
   # Función para extraer los actores y objetos de la oración
   def extraer_elementos(oracion, verbo):
      # Expresiones regulares para identificar el actor, objeto y receptor
      patron = re.compile(r'(?P<actor>\w+)\s+le\s+' + verbo + r'\s+(?P<objeto>.+?)\s+a\s+(?P<receptor>\w+)', re.IGNORECASE)
      coincidencia = patron.search(oracion)
      if coincidencia:
         return coincidencia.group('actor'), coincidencia.group('objeto'), coincidencia.group('receptor')
      else:
         # Otro patrón para oraciones como "Mauricio empujó a Jairo"
         patron_simple = re.compile(r'(?P<actor>\w+)\s+' + verbo + r'\s+a\s+(?P<receptor>\w+)', re.IGNORECASE)
         coincidencia_simple = patron_simple.search(oracion)
         if coincidencia_simple:
            return coincidencia_simple.group('actor'), None, coincidencia_simple.group('receptor')
         else:
            # Patrón para oraciones como "Jairo tomó un libro de Aaron"
            patron_tomo = re.compile(r'(?P<actor>\w+)\s+' + verbo + r'\s+(?P<objeto>.+?)\s+de\s+(?P<receptor>\w+)', re.IGNORECASE)
            coincidencia_tomo = patron_tomo.search(oracion)
            if coincidencia_tomo:
                  return coincidencia_tomo.group('actor'), coincidencia_tomo.group('objeto'), coincidencia_tomo.group('receptor')
      return None, None, None
   
   # Procesar cada oración
   for oracion in oraciones:
      accion, verbo = identificar_accion(oracion)
      if accion:
         actor, objeto, receptor = extraer_elementos(oracion, verbo)
         if accion == 'ATRANS':
            print(f"{Colores.AMARILLO_CLARO + actor + Colores.AZUL_CLARO} transfirió objeto a {Colores.VERDE_CLARO + receptor + Colores.DEFAULT}")
         elif accion == 'MTRANS':
            print(f"{Colores.AMARILLO_CLARO + actor + Colores.AZUL_CLARO} transfirió información a {Colores.VERDE_CLARO + receptor + Colores.DEFAULT}")
         elif accion == 'PROPEL':
            print(f"{Colores.AMARILLO_CLARO + actor + Colores.AZUL_CLARO} aplicó fuerza a {Colores.VERDE_CLARO + receptor + Colores.DEFAULT}")
         elif accion == 'GRASP':
            print(f"{Colores.AMARILLO_CLARO + actor + Colores.AZUL_CLARO} sostuvo objeto de {Colores.VERDE_CLARO + receptor + Colores.DEFAULT}")
      else:
         print(Colores.ROJO + "No se pudo identificar la acción en la oración: " + oracion)
   print()

def script_pacient_cares():
   # Definición de frames con recomendaciones según la hora del día
   frames = {
      "mañana": {
         "rango": range(5, 12),
         "recomendaciones": [
               "Medir la glucosa en ayunas.",
               "Desayunar antes de las 8:00 AM.",
               "Tomar la medicación matutina.",
               "Realizar actividad física ligera.",
               "Evitar bebidas azucaradas."
         ]
      },
      "tarde": {
         "rango": range(12, 18),
         "recomendaciones": [
               "Almorzar entre las 12:00 PM y 1:00 PM.",
               "Medir la glucosa 2 horas después de comer.",
               "Tomar la medicación vespertina si aplica.",
               "Evitar comidas con alto contenido calórico.",
               "Realizar una caminata breve después de comer."
         ]
      },
      "noche": {
         "rango": range(18, 24),
         "recomendaciones": [
               "Cenar antes de las 7:00 PM.",
               "Evitar alimentos ricos en carbohidratos simples.",
               "Medir la glucosa antes de acostarse.",
               "Preparar los medicamentos para el día siguiente.",
               "Evitar el consumo de cafeína y alcohol."
         ]
      },
      "madrugada": {
         "rango": range(0, 5),
         "recomendaciones": [
               "Si se despierta, evitar comer a menos que sea necesario.",
               "Mantener el ambiente propicio para el sueño.",
               "Consultar al médico si hay hipoglucemia nocturna frecuente."
         ]
      }
   }

   hora_actual = datetime.datetime.now().hour
   print(f"\nHora actual: " + Colores.AMARILLO + f"{hora_actual}:00 {Colores.DEFAULT}")

   # Determinar el frame correspondiente
   for periodo, datos in frames.items():
      if hora_actual in datos["rango"]:
         print(Colores.AMARILLO + f"Recomendaciones para la {periodo}: {Colores.DEFAULT}")
         for recomendacion in datos["recomendaciones"]:
            print(f"- {recomendacion}")
         break
   print()
