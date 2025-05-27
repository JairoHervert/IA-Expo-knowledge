from lib.consola import gotoxy, enable_ansi_escape, clrscr
from lib.diseno import print_letra, colorDefault, customForeground
from lib.menus import menu_principal, titulo_logica_1er_orden, titulo_razonamiento_reglas, titulo_llenado_ranuras, titulo_conocimiento_incierto_incompleto
"""
sintomas = [
    "No enciende",
    "Hace ruidos al iniciar",
    "Se detiene de manera inesperada",
    "Se reinicia continuamente",
    "Tiene problemas de RAM",
    "Tiene problemas en el disco duro",
    "Tiene un problema de espacio",
    "Tiene virus",
    "Tiene muchos programas instalados",
    "Tiene problemas en el procesador",
    "Tiene problemas en la tarjeta madre",
    "Tiene problemas con la fuente de energía",
    "Tiene problemas en la instalación de la tarjeta",
    "El sistema está lento",
    "La PC emite pitidos al iniciar",
    "El sistema operativo no arranca",
    "No tiene acceso a internet",
    "El sistema se congela",
    "Hace pitidos al encender",
    "Tiene problemas de temperatura alta",
]
"""

sintomas = [
    "No enciende",
    "Tiene virus",
    "La PC se calienta mucho",
    "No hace sonidos al encender",
    "La PC emite pitidos al iniciar",
    "Se apaga después de mucho uso",
    "El sistema está lento",
    "El sistema se reinicia continuamente",
    "El sistema se congela",
    "El sistema operativo se cierra solo",
    "El Sistema operativo no arranca",
    "Tiene problemas con la fuente de energía",
    "Tiene un problema de espacio",
    "Tiene problemas en el disco duro",
    "Tiene problemas de RAM",
    "Tiene problemas en el procesador",
    "Tiene problemas en la tarjeta madre",
    "Tiene muchos programas instalados",
    "Disco duro hace ruidos extraños",
    "No tiene acceso a internet",
    "Otros dispositivos sí tienen internet",
    "Ningún dispositivo tiene internet",
]

reglas = [
    # Problemas de energía y encendido
    {"si": {"No enciende", "Tiene problemas con la fuente de energía"}, "entonces": "Requiere cambio de fuente"},
    {"si": {"No enciende", "No hace sonidos al encender"}, "entonces": "Posible problema en la tarjeta madre"},
    {"si": {"No enciende", "La PC emite pitidos al iniciar"}, "entonces": "Tiene problemas de RAM"},
    {"si": {"No enciende", "Tiene virus"}, "entonces": "Requiere revisión especializada"},
    # Problemas de almacenamiento y disco duro
    {"si": {"Tiene un problema de espacio", "Tiene virus"}, "entonces": "Requiere antivirus"},
    {"si": {"Tiene un problema de espacio", "Tiene muchos programas instalados"}, "entonces": "Requiere limpieza de archivos y liberación de espacio"},
    {"si": {"Disco duro hace ruidos extraños"}, "entonces": "Tiene problemas en el disco duro"},
    {"si": {"El Sistema operativo no arranca", "Tiene problemas en el disco duro"}, "entonces": "Requiere reinstalación o cambio de disco"},
    {"si": {"El sistema está lento", "Tiene un problema de espacio"}, "entonces": "Requiere limpieza de archivos y liberación de espacio"},
    {"si": {"Tiene problemas en el disco duro"}, "entonces": "Requiere cambio o ampliación de disco duro"},
    # Problemas de RAM
    {"si": {"Tiene problemas de RAM", "El sistema está lento"}, "entonces": "Requiere aumento de RAM"},
    {"si": {"Tiene problemas de RAM", "El sistema se reinicia continuamente"}, "entonces": "Requiere cambio o limpieza de RAM"},
    {"si": {"El sistema se congela", "Tiene problemas de RAM"}, "entonces": "Posible daño en módulos de RAM"},
    {"si": {"La PC emite pitidos al iniciar"}, "entonces": "Revisar conexión o estado de RAM"},
    # Problemas fuertes
    {"si": {"Tiene problemas en el procesador"}, "entonces": "Requiere revisión especializada"},
    {"si": {"Tiene problemas en la tarjeta madre"}, "entonces": "Requiere revisión especializada"},
    # Problemas de Software / SO
    {"si": {"El sistema operativo se cierra solo"}, "entonces": "Requiere revisión de software o drivers"},
    {"si": {"Tiene virus", "El Sistema operativo no arranca"}, "entonces": "Reinstalación completa del sistema"},
    {"si": {"Tiene muchos programas instalados", "El sistema está lento"}, "entonces": "Requiere limpieza de archivos y liberación de espacio"},
    # Problemas de red
    {"si": {"No tiene acceso a internet", "Otros dispositivos sí tienen internet"}, "entonces": "Requiere revisión de drivers de red"},
    {"si": {"No tiene acceso a internet", "Ningún dispositivo tiene internet"}, "entonces": "Revisar conexión del proveedor de internet"},
    # Problemas generales
    {"si": {"La PC se calienta mucho"}, "entonces": "Requiere limpieza de ventiladores y pasta térmica"},
    {"si": {"Se apaga después de mucho uso", "La PC se calienta mucho"}, "entonces": "Posible falla de refrigeración"},
    {"si": {"Tiene problemas en el procesador", "La PC se calienta mucho"}, "entonces": "Posible falla de disipador térmico o ventilador"},

]


def motor_inferencia(hechos_iniciales, reglas):
    hechos = set(hechos_iniciales)
    nuevos_hechos = True
    primera_regla = True
    while nuevos_hechos:
        nuevos_hechos = False
        for regla in reglas:
            # Si todos los hechos en la parte "si" están en los hechos actuales
            if regla["si"].issubset(hechos) and regla["entonces"] not in hechos:
                hechos.add(regla["entonces"])
                if(primera_regla == True):
                    print("\n   \033[96mReglas aplicadas:\033[0m ")
                    primera_regla = False
                print(f"\033[94mSi \033[0m{regla['si']}\033[94m entonces \033[0m{regla['entonces']}")
                nuevos_hechos = True

    return hechos

def analisis_PC():
    hechos_iniciales = set()

    while True:
        clrscr()
        titulo_razonamiento_reglas((255, 198, 64), (255, 146, 64), (189, 15, 17))
        
        print("\n   Introduzca un número para marcar o desmarcar el problema.\n")
        index = 0
        while(index < len(sintomas)):
            string = " " + str(index+1) + ". "
            if sintomas[index] in hechos_iniciales:
                string += "(\033[92mV\033[0m) "
            else:
                string += "(\033[91mF\033[0m) "
            print(string+sintomas[index])
            index+=1

        resultado = motor_inferencia(hechos_iniciales, reglas)
        print("\n   \033[96mHechos nuevos deducidos:\033[0m")
        hechos_derivados = resultado - hechos_iniciales
        for hecho in hechos_derivados:
            print(f" - {hecho}")
        
        opcion = input("Introduzca un número o escriba \"salir\" para terminar con el programa: ")
        if(opcion == "salir"):
            break
        elif opcion.isdigit():
            idx = int(opcion)
            if 1 <= idx <= len(sintomas):
                sintoma = sintomas[idx - 1]
                if sintoma in hechos_iniciales:
                    hechos_iniciales.remove(sintoma)
                else:
                    hechos_iniciales.add(sintoma)


