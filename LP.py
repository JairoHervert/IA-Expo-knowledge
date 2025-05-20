# -*- coding: utf-8 -*-

import pygame
import sys
from sympy import symbols, Implies, And, Or, Not


# Inicializar PyGame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lógica del Guerrero - IA con Lógica Proposicional")

try:
    font = pygame.font.Font("DejaVuSans.ttf", 24)  # Tamaño 24
    small_font = pygame.font.Font("DejaVuSans.ttf", 18)  # Tamaño 18
except FileNotFoundError:
    print("¡Error: Archivo de fuente no encontrado! Usando fuente predeterminada.")
    font = pygame.font.SysFont("Arial", 24)  # Fallback

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fuente
font = pygame.font.SysFont("Arial", 24)
small_font = pygame.font.SysFont("Arial", 18)

# Predicados (Lógica de Primer Orden)
es_debil, salud_suf, tiene_poc = symbols('es_debil salud_suf tiene_poc')

# Reglas Lógicas (usando SymPy)
regla_atacar = Implies(And(es_debil, salud_suf), "ATACAR")
regla_huir = Implies(Or(Not(es_debil), Not(salud_suf)), "HUIR")
regla_curarse = Implies(And(Not(salud_suf), tiene_poc), "CURARSE")

# Estado del juego
estado = {
    "es_debil": False,
    "salud_suf": True,
    "tiene_poc": False,
    "accion": None
}

def evaluar_accion():
    if estado["es_debil"] and estado["salud_suf"]:
        estado["accion"] = "ATACAR"
    elif (not estado["es_debil"] or not estado["salud_suf"]):
        if not estado["salud_suf"] and estado["tiene_poc"]:
            estado["accion"] = "CURARSE"
        else:
            estado["accion"] = "HUIR"
    else:
        estado["accion"] = "NO_ACCION"

def dibujar_interfaz():
    screen.fill(WHITE)
    
    # Título
    titulo = font.render("Lógica del Guerrero - Toma de Decisiones", True, BLACK)
    screen.blit(titulo, (width // 2 - titulo.get_width() // 2, 20))
    
    # Estado actual
    pygame.draw.rect(screen, BLACK, (50, 80, 700, 150), 2)
    estado_text = font.render("Estado Actual:", True, BLACK)
    screen.blit(estado_text, (60, 90))
    
    debil_text = small_font.render(f"Enemigo es débil: {estado['es_debil']}", True, BLACK)
    salud_text = small_font.render(f"Salud suficiente: {estado['salud_suf']}", True, BLACK)
    pocion_text = small_font.render(f"Tiene poción: {estado['tiene_poc']}", True, BLACK)
    screen.blit(debil_text, (60, 130))
    screen.blit(salud_text, (60, 160))
    screen.blit(pocion_text, (60, 190))
    
    # Reglas Lógicas (SymPy)
    pygame.draw.rect(screen, BLACK, (50, 250, 700, 200), 2)
    logica_text = font.render("Reglas Lógicas (Primer Orden):", True, BLACK)
    screen.blit(logica_text, (60, 260))
    
    regla1 = small_font.render(f"1. Si (es_debil Y salud_suf) → ATACAR", True, BLUE)
    regla2 = small_font.render(f"2. Si (¬es_debil O ¬salud_suf) → HUIR", True, BLUE)
    regla3 = small_font.render(f"3. Si (¬salud_suf Y tiene_poc) → CURARSE", True, BLUE)
    screen.blit(regla1, (60, 300))
    screen.blit(regla2, (60, 330))
    screen.blit(regla3, (60, 360))
    
    # Acción elegida
    pygame.draw.rect(screen, BLACK, (50, 470, 700, 80), 2)
    accion_text = font.render(f"Decisión del Guerrero:", True, BLACK)
    screen.blit(accion_text, (60, 480))
    
    if estado["accion"]:
        accion = font.render(estado["accion"], True, GREEN if estado["accion"] == "ATACAR" else RED if estado["accion"] == "HUIR" else YELLOW)
        screen.blit(accion, (60, 520))
    
    # Botones para cambiar estado
    pygame.draw.rect(screen, GREEN if estado["es_debil"] else RED, (200, 100, 120, 40))
    debil_btn = small_font.render("Enemigo Débil", True, WHITE)
    screen.blit(debil_btn, (210, 110))
    
    pygame.draw.rect(screen, GREEN if estado["salud_suf"] else RED, (400, 100, 150, 40))
    salud_btn = small_font.render("Salud Suficiente", True, WHITE)
    screen.blit(salud_btn, (410, 110))
    
    pygame.draw.rect(screen, GREEN if estado["tiene_poc"] else RED, (600, 100, 120, 40))
    pocion_btn = small_font.render("Tiene Poción", True, WHITE)
    screen.blit(pocion_btn, (610, 110))
    
    pygame.display.flip()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Cambiar estado con clics
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Botón "Enemigo Débil"
            if 200 <= mouse_pos[0] <= 320 and 100 <= mouse_pos[1] <= 140:
                estado["es_debil"] = not estado["es_debil"]
            
            # Botón "Salud Suficiente"
            if 400 <= mouse_pos[0] <= 550 and 100 <= mouse_pos[1] <= 140:
                estado["salud_suf"] = not estado["salud_suf"]
            
            # Botón "Tiene Poción"
            if 600 <= mouse_pos[0] <= 720 and 100 <= mouse_pos[1] <= 140:
                estado["tiene_poc"] = not estado["tiene_poc"]
            
            evaluar_accion()
    
    dibujar_interfaz()

pygame.quit()
sys.exit()