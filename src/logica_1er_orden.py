# -*- coding: utf-8 -*-
import pygame
import random
import time
import sys
from pygame import mixer

def batalla_estrategica():
    # Inicialización
    pygame.init()
    mixer.init()
    width, height = 1280, 720  # Mayor resolución
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lógica del Guerrero - Batalla Estratégica")

    # Colores
    WHITE = (240, 240, 240)
    BLACK = (30, 30, 30)
    RED = (220, 60, 60)
    GREEN = (70, 200, 80)
    BLUE = (60, 120, 220)
    YELLOW = (255, 220, 80)
    PURPLE = (150, 80, 220)

    # Fuentes
    try:
        font_title = pygame.font.Font("DejaVuSans-Bold.ttf", 42)
        font_large = pygame.font.Font("DejaVuSans.ttf", 32)
        font_medium = pygame.font.Font("DejaVuSans.ttf", 24)
        font_small = pygame.font.Font("DejaVuSans.ttf", 18)
    except:
        font_title = pygame.font.SysFont("arial", 42, bold=True)
        font_large = pygame.font.SysFont("arial", 32)
        font_medium = pygame.font.SysFont("arial", 24)
        font_small = pygame.font.SysFont("arial", 18)

    # Cargar imágenes (ejemplo con formas básicas)
    def load_image(color, size):
        surf = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(surf, color, (0, 0, *size), 0, 10)  # Rectángulo redondeado
        return surf

    # Crear sprites con mejores gráficos
    class Warrior(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = load_image(BLUE, (120, 120))
            # Icono de guerrero
            pygame.draw.polygon(self.image, WHITE, [(60, 20), (30, 100), (90, 100)])
            self.rect = self.image.get_rect(center=(400, 400))
            self.health = 100
            self.max_health = 100
            self.attack_power = 25
        
        def draw_health(self, surface):
            ratio = self.health / self.max_health
            # Barra de vida con fondo
            pygame.draw.rect(surface, (80, 80, 80), (self.rect.x-10, self.rect.y-30, 140, 20), 0, 5)
            pygame.draw.rect(surface, GREEN if ratio > 0.3 else RED, 
                            (self.rect.x-10, self.rect.y-30, 140 * ratio, 20), 0, 5)
            pygame.draw.rect(surface, BLACK, (self.rect.x-10, self.rect.y-30, 140, 20), 2, 5)
            
            # Texto de salud
            health_text = font_small.render(f"{self.health}/{self.max_health}", True, WHITE)
            surface.blit(health_text, (self.rect.x + 60 - health_text.get_width()//2, self.rect.y-28))

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = load_image(RED, (100, 100))
            # Icono de monstruo
            pygame.draw.circle(self.image, WHITE, (50, 40), 15)  # Cabeza
            pygame.draw.ellipse(self.image, WHITE, (30, 60, 40, 30))  # Cuerpo
            self.rect = self.image.get_rect(center=(880, 400))
            self.health = 150
            self.max_health = 150
            self.is_weak = False
            self.attack_power = 20
        
        def update_health(self, surface):
            ratio = self.health / self.max_health
            # Barra de vida
            pygame.draw.rect(surface, (80, 80, 80), (self.rect.x-10, self.rect.y-30, 120, 20), 0, 5)
            color = GREEN if self.is_weak else PURPLE
            pygame.draw.rect(surface, color, (self.rect.x-10, self.rect.y-30, 120 * ratio, 20), 0, 5)
            pygame.draw.rect(surface, BLACK, (self.rect.x-10, self.rect.y-30, 120, 20), 2, 5)
            
            # Texto de salud
            health_text = font_small.render(f"{self.health}/{self.max_health}", True, WHITE)
            surface.blit(health_text, (self.rect.x + 50 - health_text.get_width()//2, self.rect.y-28))

    # Estado del juego
    warrior = Warrior()
    enemy = Enemy()

    game_state = {
        "turno": 1,
        "en_batalla": True,
        "log_actions": [],
        "delay_entre_acciones": 2.5,
        "tiene_pocion": True,
        "pociones": 2,
        "action": None,
        "warrior_hit": False,
        "enemy_hit": False,
        "animation_timer": 0,
        "game_over": False,
        "victory": False
    }

    # Panel de información
    class InfoPanel:
        def __init__(self):
            self.width = 400
            self.height = 200
            self.rect = pygame.Rect(width - self.width - 20, 20, self.width, self.height)
            self.title = "Reglas de Combate:"
            self.rules = [
                "1. Salud < 30% + Poción → CURARSE",
                "2. Salud < 30% sin Poción → HUIR",
                "3. Enemigo débil → ATACAR",
                "4. Enemigo fuerte → ANALIZAR"
            ]
        
        def draw(self, surface):
            # Fondo del panel
            pygame.draw.rect(surface, (50, 50, 70), self.rect, 0, 10)
            pygame.draw.rect(surface, BLUE, self.rect, 3, 10)
            
            # Título
            title_text = font_medium.render(self.title, True, WHITE)
            surface.blit(title_text, (self.rect.x + 20, self.rect.y + 15))
            
            # Reglas
            for i, rule in enumerate(self.rules):
                rule_text = font_small.render(rule, True, WHITE)
                surface.blit(rule_text, (self.rect.x + 30, self.rect.y + 50 + i * 30))

    info_panel = InfoPanel()

    # Función de batalla mejorada
    def batalla_automatica():
        UMBRAL_CRITICO = 0.3
        
        game_state["log_actions"].append(f"--- Turno {game_state['turno']} ---")
        
        # Lógica mejorada del Guerrero
        if warrior.health < UMBRAL_CRITICO * warrior.max_health and game_state["pociones"] > 0:
            action = "CURARSE"
            heal_amount = min(50, warrior.max_health - warrior.health)
            warrior.health += heal_amount
            game_state["pociones"] -= 1
            log_msg = f"Regla 1: (Salud <30% + Poción) → CURARSE (+{heal_amount} HP)"
        
        elif warrior.health < UMBRAL_CRITICO * warrior.max_health:
            action = "HUIR"
            log_msg = "Regla 2: (Salud <30% sin Poción) → HUIR"
        
        elif enemy.is_weak:
            action = "ATACAR"
            damage = random.randint(warrior.attack_power-5, warrior.attack_power+5)
            enemy.health = max(0, enemy.health - damage)
            game_state["enemy_hit"] = True
            log_msg = f"Regla 3: (Enemigo débil) → ATACAR (-{damage} HP)"
        
        else:
            action = "ANALIZAR"
            # 50% de probabilidad de encontrar debilidad
            if random.random() < 0.5:
                enemy.is_weak = True
                log_msg = "Regla 4: (Enemigo fuerte) → ANALIZAR (¡Descubrió debilidad!)"
            else:
                log_msg = "Regla 4: (Enemigo fuerte) → ANALIZAR (No encontró debilidad)"
        
        game_state["action"] = action
        game_state["log_actions"].append(f"Guerrero: {action}")
        game_state["log_actions"].append(log_msg)
        
        # Turno del enemigo (si no ha huido y sigue vivo)
        if action != "HUIR" and enemy.health > 0 and not game_state["game_over"]:
            enemy_damage = random.randint(enemy.attack_power-5, enemy.attack_power+5)
            warrior.health = max(0, warrior.health - enemy_damage)
            game_state["log_actions"].append(f"Enemigo: Contraataca (-{enemy_damage} HP)")
            game_state["warrior_hit"] = True
        
        # Actualizar estado del juego
        game_state["animation_timer"] = 15  # Frames de animación
        game_state["turno"] += 1
        
        # Verificar condiciones de fin de juego
        if warrior.health <= 0:
            game_state["log_actions"].append("¡El guerrero ha sido derrotado!")
            game_state["game_over"] = True
        elif enemy.health <= 0:
            game_state["log_actions"].append("¡Enemigo derrotado!")
            game_state["victory"] = True
        elif action == "HUIR":
            game_state["log_actions"].append("¡El guerrero ha huido!")
            game_state["game_over"] = True

    # Bucle principal mejorado
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (game_state["game_over"] or game_state["victory"]):
                    # Reiniciar juego
                    warrior = Warrior()
                    enemy = Enemy()
                    enemy.is_weak = random.choice([True, False])
                    game_state = {
                        "turno": 1,
                        "en_batalla": True,
                        "log_actions": [],
                        "delay_entre_acciones": 1.8,
                        "tiene_pocion": True,
                        "pociones": 2,
                        "action": None,
                        "warrior_hit": False,
                        "enemy_hit": False,
                        "animation_timer": 0,
                        "game_over": False,
                        "victory": False
                    }
        
        # Dibujado
        screen.fill(WHITE)
        
        # Fondo decorativo
        pygame.draw.rect(screen, (230, 230, 240), (0, 0, width, height//2))
        pygame.draw.rect(screen, (200, 230, 200), (0, height//2, width, height//2))
        
        # Animaciones
        if game_state["animation_timer"] > 0:
            game_state["animation_timer"] -= 1
            
            if game_state["warrior_hit"]:
                # Efecto de golpe al guerrero
                if game_state["animation_timer"] % 5 < 3:
                    warrior.image.fill(RED, special_flags=pygame.BLEND_MULT)
            
            if game_state["enemy_hit"]:
                # Efecto de golpe al enemigo
                if game_state["animation_timer"] % 5 < 3:
                    enemy.image.fill(RED, special_flags=pygame.BLEND_MULT)
        
        # Dibujar personajes
        screen.blit(warrior.image, warrior.rect)
        screen.blit(enemy.image, enemy.rect)
        
        # Dibujar barras de vida
        warrior.draw_health(screen)
        enemy.update_health(screen)
        
        # Panel de información
        info_panel.draw(screen)
        
        # Panel de registro de acciones
        pygame.draw.rect(screen, (240, 240, 250), (20, 20, 450, 200), 0, 10)
        pygame.draw.rect(screen, BLACK, (20, 20, 450, 200), 2, 10)
        
        title_text = font_medium.render("Registro de Batalla:", True, BLACK)
        screen.blit(title_text, (40, 30))
        
        y_offset = 60
        for log in game_state["log_actions"][-6:]:
            log_text = font_small.render(log, True, BLACK)
            screen.blit(log_text, (40, y_offset))
            y_offset += 25
        
        # Panel de estado
        pygame.draw.rect(screen, (240, 240, 250), (20, height-120, 300, 100), 0, 10)
        pygame.draw.rect(screen, BLACK, (20, height-120, 300, 100), 2, 10)
        
        turno_text = font_medium.render(f"Turno: {game_state['turno']}", True, BLACK)
        screen.blit(turno_text, (40, height-100))
        
        pociones_text = font_medium.render(f"Pociones: {game_state['pociones']}", True, BLUE)
        screen.blit(pociones_text, (40, height-70))
        
        # Indicador de debilidad del enemigo
        debil_text = font_medium.render(
            f"Enemigo: {'DÉBIL' if enemy.is_weak else 'FUERTE'}", 
            True, GREEN if enemy.is_weak else PURPLE
        )
        screen.blit(debil_text, (width//2 - debil_text.get_width()//2, 30))
        
        # Batalla automática
        if game_state["en_batalla"] and not game_state["game_over"] and not game_state["victory"]:
            pygame.display.flip()
            time.sleep(game_state["delay_entre_acciones"])
            batalla_automatica()
        else:
            # Mensaje de fin de juego
            if game_state["victory"]:
                result_text = font_title.render("¡VICTORIA!", True, GREEN)
                screen.blit(result_text, (width//2 - result_text.get_width()//2, height//2 - 50))
            else:
                result_text = font_title.render("¡DERROTA!", True, RED)
                screen.blit(result_text, (width//2 - result_text.get_width()//2, height//2 - 50))
            
            restart_text = font_medium.render("Presiona ESPACIO para reiniciar", True, BLACK)
            screen.blit(restart_text, (width//2 - restart_text.get_width()//2, height//2 + 20))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    #sys.exit()