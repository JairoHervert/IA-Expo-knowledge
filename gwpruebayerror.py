import pygame
import numpy as np
import random
import time

# Parámetros del entorno
ROWS, COLS = 6, 6
CELL_SIZE = 80
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

# Colores
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
PATH_COLOR = (200, 230, 255)

# Mapa
start = (0, 0)
goal = (5, 5)
walls = [(1, 1), (2, 1), (3, 1), (4, 2)]
obstacles = [(2, 3), (3, 4), (4, 4)]
blocked = set(walls + obstacles)

# Acciones: [UP, DOWN, LEFT, RIGHT]
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
num_actions = len(actions)

# Inicializar Q-table
Q = np.zeros((ROWS, COLS, num_actions))

# Hiperparámetros
alpha = 0.1      # Tasa de aprendizaje
gamma = 0.95     # Factor de descuento
epsilon = 0.3    # Exploración
episodes = 100   # Número de episodios de entrenamiento
max_steps = 50

# Recompensas
def get_reward(state):
    if state == goal:
        return 10
    elif state in obstacles or state in walls:
        return -10
    else:
        return -1

# Inicializa Pygame para visualización
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid World - Q-learning")
clock = pygame.time.Clock()

# Dibujar el grid
def draw_grid(agent_pos, path):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pos = (row, col)
            if pos == agent_pos:
                pygame.draw.rect(screen, BLUE, rect)
            elif pos == goal:
                pygame.draw.rect(screen, GREEN, rect)
            elif pos in walls:
                pygame.draw.rect(screen, GRAY, rect)
            elif pos in obstacles:
                pygame.draw.rect(screen, RED, rect)
            elif pos in path:
                pygame.draw.rect(screen, PATH_COLOR, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Elegir acción con política epsilon-greedy
def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.randint(num_actions)
    else:
        return np.argmax(Q[state[0], state[1]])

# Entrenamiento con visualización por episodio
for episode in range(episodes):
    state = start
    trajectory = [state]
    print(f"\n🌀 Episodio {episode + 1}")

    for step in range(max_steps):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        action = choose_action(state)
        move = actions[action]
        new_state = (state[0] + move[0], state[1] + move[1])

        # Verificar límites
        if not (0 <= new_state[0] < ROWS and 0 <= new_state[1] < COLS):
            print("❌ Movimiento fuera de los límites.")
            new_state = state

        reward = get_reward(new_state)
        best_next = np.max(Q[new_state[0], new_state[1]])
        Q[state[0], state[1], action] += alpha * (reward + gamma * best_next - Q[state[0], state[1], action])
        
        trajectory.append(new_state)
        state = new_state

        # Dibujar
        screen.fill(WHITE)
        draw_grid(state, trajectory)
        pygame.display.flip()
        clock.tick(8)

        # Condiciones de parada
        if state in walls:
            print("💥 Choque contra una pared.")
            break
        elif state in obstacles:
            print("💢 Choque contra un obstáculo.")
            break
        elif state == goal:
            print("✅ ¡Agente ha llegado a la meta!")
            break

print("\n🏁 Entrenamiento finalizado.")
pygame.time.wait(2000)
pygame.quit()
