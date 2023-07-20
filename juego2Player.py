from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
import os
import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana del juego
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game Multijugador")

# Colores
green = (0, 128, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# Tamaño de los segmentos del gusano y velocidad
segment_size = 20
segment_speed = 20

clock = pygame.time.Clock()

def game_loop():
    game_over = False
    game_exit = False

    # Posición inicial del gusano
    head_x = window_width / 2
    head_y = window_height / 2

    # Inicializar el gusano como una lista de segmentos
    segments = [(head_x, head_y)]
    for _ in range(2):
        segments.append((segments[-1][0] - segment_size, segments[-1][1]))

    # Generar una posición aleatoria para la manzana
    point_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
    point_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size

    # Variables para controlar la dirección y velocidad del gusano
    change_x = segment_size
    change_y = 0
    last_key = pygame.K_RIGHT

    while not game_exit:
        while game_over:
            # Pantalla de game over
            window.fill(black)
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over", True, red)
            window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 - text.get_height() / 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_exit = True
                    elif event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key != pygame.K_RIGHT:
                    last_key = pygame.K_LEFT
                    change_x = -segment_speed
                    change_y = 0
                elif event.key == pygame.K_RIGHT and last_key != pygame.K_LEFT:
                    last_key = pygame.K_RIGHT
                    change_x = segment_speed
                    change_y = 0
                elif event.key == pygame.K_UP and last_key != pygame.K_DOWN:
                    last_key = pygame.K_UP
                    change_x = 0
                    change_y = -segment_speed
                elif event.key == pygame.K_DOWN and last_key != pygame.K_UP:
                    last_key = pygame.K_DOWN
                    change_x = 0
                    change_y = segment_speed

        # Actualizar la posición de la cabeza del gusano
        head_x += change_x
        head_y += change_y

        # Verificar si el gusano chocó contra los bordes de la ventana
        if head_x >= window_width or head_x < 0 or head_y >= window_height or head_y < 0:
            game_over = True

        # Actualizar la ventana
        window.fill(black)

        # Dibujar el punto
        pygame.draw.rect(window, red, (point_x, point_y, segment_size, segment_size))

        # Dibujar el gusano
        for segment in segments:
            pygame.draw.rect(window, green, (segment[0], segment[1], segment_size, segment_size))

        # Agregar la nueva posición de la cabeza del gusano a la lista de segmentos
        segments.append((head_x, head_y))

        # Verificar si el gusano alcanzó el punto
        if head_x == point_x and head_y == point_y:
            # Generar una nueva posición aleatoria para la manzana
            while (point_x, point_y) in segments:
                point_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
                point_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
        else:
            # Si no se alcanzó el punto, eliminar el último segmento del gusano
            segments.pop(0)

        # Verificar si el gusano chocó consigo mismo
        if (head_x, head_y) in segments[:-1]:
            game_over = True

        pygame.display.update()
        clock.tick(10)  # Velocidad del juego (10 cuadros por segundo)

    pygame.quit()
    quit()

game_loop()
