import pygame
import sys
import heapq

# Parámetros del grid
ROWS, COLS = 10, 10
CELL_SIZE = 50
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

# Colores
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid World - A* Pathfinding")
clock = pygame.time.Clock()

# Definir posiciones
start = (0, 0)
goal = (9, 9)
walls = [(1, 1), (2, 1), (3, 1), (4, 4), (5, 4)]
obstacles = [(0, 5), (3, 6), (7, 2), (8, 8)]
blocked = set(walls + obstacles)

# Direcciones de movimiento
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# A* Search
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, []))
    visited = set()

    while open_set:
        f, cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        path = path + [current]
        if current == goal:
            return path
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and
                neighbor not in blocked and neighbor not in visited):
                heapq.heappush(open_set, (cost + 1 + heuristic(neighbor, goal), cost + 1, neighbor, path))
    return None

# Dibujar la cuadrícula
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
            elif pos in path and pos != start and pos != goal:
                pygame.draw.rect(screen, (180, 220, 255), rect)  # Ruta
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

# Calcular ruta al inicio
path = a_star(start, goal)
if not path:
    print("¡No se encontró camino!")
    pygame.quit()
    sys.exit()

print("Ruta encontrada:")
print(path)

step = 0
running = True
while running:
    clock.tick(4)  # Velocidad de movimiento

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if step < len(path):
        agent_pos = path[step]
        screen.fill(WHITE)
        draw_grid(agent_pos, path)
        pygame.display.flip()
        step += 1

        if agent_pos in walls:
            print("¡Choque contra una pared!")
        elif agent_pos in obstacles:
            print("¡Choque contra un obstáculo!")
        elif agent_pos == goal:
            print("¡Agente ha llegado a la meta!")

pygame.quit()
sys.exit()
