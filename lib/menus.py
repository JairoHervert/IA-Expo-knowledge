from .consola import gotoxy, enable_ansi_escape, clrscr
from .diseno import print_letra, colorDefault

def menu_principal(color1, color2, color3):
    posX = 15
    posY = 2
    posX += print_letra('3', posX, posY, color1, color2, color3)
    posX += print_letra('.', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('M', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('T', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    print("\n   Seleccionar un tema.\n")
    print("  1.- 3.2 Lógica de primer orden")
    print("  2.- 3.3 Razonamiento basado en reglas")
    print("  3.- 3.4 Modelos de llenado de ranuras")
    print("  4.- 3.5 Modelos de conocimiento incierto e incompleto")
    print("  5.- Salir")

def titulo_llenado_ranuras(color1, color2, color3):
    posX = 3
    posY = 2
    posX += print_letra('3', posX, posY, color1, color2, color3)
    posX += print_letra('.', posX, posY, color1, color2, color3)
    posX += print_letra('4', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('L', posX, posY, color1, color2, color3)
    posX += print_letra('L', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('D', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('D', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('U', posX, posY, color1, color2, color3)
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('S', posX, posY, color1, color2, color3)

def titulo_logica_1er_orden(color1, color2, color3):
    posX = 28
    posY = 2
    posX += print_letra('3', posX, posY, color1, color2, color3)
    posX += print_letra('.', posX, posY, color1, color2, color3)
    posX += print_letra('2', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('L', posX, posY, color1, color2, color3)
    posX += print_letra('Ó', posX, posY, color1, color2, color3)
    posX += print_letra('G', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('D', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX = 28
    posY = 7
    posX += print_letra('P', posX, posY, color1, color2, color3)
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('M', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('D', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)

def titulo_razonamiento_reglas(color1, color2, color3):
    posX = 15
    posY = 2
    posX += print_letra('3', posX, posY, color1, color2, color3)
    posX += print_letra('.', posX, posY, color1, color2, color3)
    posX += print_letra('3', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('Z', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('M', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('T', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX = 18
    posY = 7
    posX += print_letra('B', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('S', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('D', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('G', posX, posY, color1, color2, color3)
    posX += print_letra('L', posX, posY, color1, color2, color3)
    posX += print_letra('A', posX, posY, color1, color2, color3)
    posX += print_letra('S', posX, posY, color1, color2, color3)

def titulo_conocimiento_incierto_incompleto(color1, color2, color3):
    posX = 15
    posY = 2
    posX += print_letra('3', posX, posY, color1, color2, color3)
    posX += print_letra('.', posX, posY, color1, color2, color3)
    posX += print_letra('5', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('M', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('T', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX = 2
    posY = 7
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('R', posX, posY, color1, color2, color3)
    posX += print_letra('T', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += 4
    posX += print_letra('I', posX, posY, color1, color2, color3)
    posX += print_letra('N', posX, posY, color1, color2, color3)
    posX += print_letra('C', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)
    posX += print_letra('M', posX, posY, color1, color2, color3)
    posX += print_letra('P', posX, posY, color1, color2, color3)
    posX += print_letra('L', posX, posY, color1, color2, color3)
    posX += print_letra('E', posX, posY, color1, color2, color3)
    posX += print_letra('T', posX, posY, color1, color2, color3)
    posX += print_letra('O', posX, posY, color1, color2, color3)