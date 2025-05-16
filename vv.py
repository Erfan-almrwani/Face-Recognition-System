
# import numpy as np
# import random

# # Define the cities and distances between them
# cities = ["City 1", "City 2", "City 3", "City 4"]
# distances = {
#     ("City 1", "City 2"): 10,
#     ("City 1", "City 3"): 15,
#     ("City 1", "City 4"): 20,
#     ("City 2", "City 3"): 35,
#     ("City 2", "City 4"): 25,
#     ("City 3", "City 4"): 30
# }

# # Define the ant
# class Ant:
#     def __init__(self, start_city):
#         self.visited_cities = [start_city]
#         self.current_city = start_city

#     def visit_city(self, city):
#         self.visited_cities.append(city)
#         self.current_city = city

# # Define the algorithm
# class AntAlgorithm:
#     def __init__(self, cities, distances, evaporation_rate=0.5, pheromone_deposit=1.0):
#         self.cities = cities
#         self.distances = distances
#         self.evaporation_rate = evaporation_rate
#         self.pheromone_deposit = pheromone_deposit
#         self.pheromones = {(city1, city2): 1.0 for city1 in cities for city2 in cities if city1 != city2}

#     def run(self, iterations=100):
#         for _ in range(iterations):
#             ants = [Ant(random.choice(self.cities)) for _ in range(len(self.cities))]
#             for ant in ants:
#                 while len(ant.visited_cities) < len(self.cities):
#                     available_cities = [city for city in self.cities if city not in ant.visited_cities]
#                     probabilities = [self.calculate_probability(ant.current_city, city) for city in available_cities]
#                     selected_city = random.choices(available_cities, weights=probabilities)[0]
#                     ant.visit_city(selected_city)
#                 self.deposit_pheromone(ant)

#             self.update_pheromones()

#     def calculate_probability(self, current_city, next_city):
#         pheromone = self.pheromones[(current_city, next_city)]
#         distance = self.distances.get((current_city, next_city), self.distances.get((next_city, current_city)))
#         total_pheromone = sum(self.pheromones[(current_city, city)] for city in self.cities if city != current_city)
#         return (pheromone ** 2) / (distance * total_pheromone)

#     def deposit_pheromone(self, ant):
#         for i in range(len(ant.visited_cities) - 1):
#             city1, city2 = ant.visited_cities[i], ant.visited_cities[i + 1]
#             self.pheromones[(city1, city2)] += self.pheromone_deposit

#     def update_pheromones(self):
#         for city1 in self.cities:
#             for city2 in self.cities:
#                 if city1 != city2:
#                     self.pheromones[(city1, city2)] *= (1 - self.evaporation_rate)

# # Run the algorithm
# algorithm = AntAlgorithm(cities, distances)
# algorithm.run()
# print("Best path:", algorithm.pheromones)

import pygame
from collections import deque
import time

# ألوان المتاهة
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# الأبعاد وحجم الخلية
WIDTH = 30
HEIGHT = 30
MARGIN = 1

# المتاهة
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# تهيئة الشاشة
pygame.init()
WINDOW_SIZE = [(WIDTH + MARGIN) * len(maze[0]) + MARGIN , (HEIGHT + MARGIN) * len(maze) + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("متاهة")

# خوارزمية BFS لحل المتاهة
def bfs(maze, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
    

        if current == goal:
            return path +[current]

        if current not in visited:
            visited.add(current)

            neighbors = get_neighbors(maze, current)
            for neighbor in neighbors:
                queue.append((neighbor, path + [current]))

        draw_maze(maze, start, goal, visited, current)
        time.sleep(0.1)  # تأخير للمحاكاة

# الحصول على الجيران الصالحين
def get_neighbors(maze, current):
    row, col = current
    neighbors = []

    # جيران الأعلى والأسفل واليسار واليمين86
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if is_valid(maze, new_row, new_col):
            neighbors.append((new_row, new_col))

    return neighbors

# التحقق من صلاحية الخلية
def is_valid(maze, row, col):
    num_rows = len(maze)
    num_cols = len(maze[0])

    if 0 <= row < num_rows and 0 <= col < num_cols and maze[row][col] == 0:
        return True
    
    return False

# رسم المتاهة والحلقة الرئيسية للعرض
# رسم المتاهة والحلقة الرئيسية للعرض
def draw_maze(maze, start, goal, visited, current):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = WHITE

            if maze[row][col] == 1:
                color = BLUE
            elif (row, col) == start:
                color = RED
            elif (row, col) == goal:
                color =GREEN
            elif (row, col) == current:
                color = BLACK
            elif (row, col) in visited:
                color = (100, 100, 100)  # لون رمادي للخلايا التي تم زيارتها

            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN,
                                             (MARGIN + HEIGHT) * row + MARGIN,
                                             WIDTH, HEIGHT])

    pygame.display.flip()

# نقاط البداية والهدف
start = (1, 1)
goal = (18,1)

# حل المتاهة باستخدام BFS
path = bfs(maze, start, goal)

# عرض المتاهة والحل
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
           draw_maze(maze, start, goal, set(path), path[-1])
    

print("path is:", path )
