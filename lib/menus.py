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

def titulo_greedy():
    print_letra('A', 15, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('L', 21, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('G', 26, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('O', 32, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('R', 38, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('I', 43, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('T', 49, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('M', 55, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('O', 63, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('G', 73, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('R', 79, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('E', 84, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('E', 89, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('D', 94, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))
    print_letra('Y', 100, 2, (255, 178, 0), (124, 178, 0), (20, 178, 0))

def titulo_hill_climbing():
    print_letra('H', 24, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('I', 30, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('L', 36, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('L', 41, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('-', 45, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('C', 50, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('L', 55, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('I', 60, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('M', 66, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('B', 74, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('I', 79, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('N', 85, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))
    print_letra('G', 92, 2, (250, 250, 250), (47, 72, 165), (135, 79, 44))

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