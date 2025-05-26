import networkx as nx
import matplotlib.pyplot as plt
import datetime
import re
from colorama import init, Fore, Back, Style

from lib.consola import gotoxy, enable_ansi_escape, clrscr
from lib.diseno import print_letra, colorDefault, customForeground
from lib.menus import menu_principal, titulo_logica_1er_orden, titulo_llenado_ranuras, titulo_conocimiento_incierto_incompleto

from src.llenado_de_ranuras import semantic_network_animals, frames_medical_diagnostics, conceptual_dependency, script_pacient_cares
from src.logica_1er_orden import batalla_estrategica
from src.conocimiento_incierto import xg_difuso

def menu_3_2():
    opcion = 0
    clrscr()
    titulo_logica_1er_orden((198, 0, 139), (0, 178, 211), (255, 236, 236))
    batalla_estrategica()
    customForeground(255,135,191)
    input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def menu_3_4():
    opcion = 0
    while(opcion != 5):
        clrscr()
        titulo_llenado_ranuras((255, 198, 64), (255, 146, 64), (189, 15, 17))
        print("\n   Seleccionar un tema.\n")
        print("  1.- Red semántica de animales")
        print("  2.- Marco de diagnóstico médico")
        print("  3.- Dependencia conceptual de oraciones")
        print("  4.- Guiones de cuidados del paciente")
        print("  5.- Regresar")
        opcion = int(input("\n   Seleccione la opción deseada: "))
        if(opcion == 1):
            semantic_network_animals()
        elif(opcion == 2):
            frames_medical_diagnostics()
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        elif(opcion == 3):
            conceptual_dependency()
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        elif(opcion == 4):
            script_pacient_cares()
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def menu_3_5():
    opcion = 0
    while(opcion != 3):
        clrscr()
        titulo_conocimiento_incierto_incompleto((254, 244, 255), (157, 151, 158), (158, 0, 13))
        print("\n   Seleccionar modo.\n")
        print("  1.- Ejemplo prediseñado")
        print("  2.- Cargar de archivo CSV")
        print("  3.- Regresar")
        opcion = int(input("\n   Seleccione la opción deseada: "))
        if(opcion == 1):
            xg_difuso(None)
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")
        elif(opcion == 2):
            ruta = input("Ingresa la ruta del archivo CSV: ").strip()
            xg_difuso(ruta)
            customForeground(255,135,191)
            input("\n   Presiona ENTER para continuar...\033[0m\n\n\n")

def main():
    # Inicializar colorama
    #init(autoreset=True)
    enable_ansi_escape()
    while True:
        clrscr()
        menu_principal((0, 57, 191), (0, 147, 191), (110, 239, 238))
        opcion = int(input("\n   Seleccione la opción deseada: "))
        if(opcion == 1):
            menu_3_2()
        elif(opcion == 2):
            print("¿")
        elif(opcion == 3):
            menu_3_4()
        elif(opcion == 4):
            menu_3_5()
        elif(opcion == 5):
            exit(0)

if __name__ == "__main__":
   main()