from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox
import os
import pygame
import random
import pygame.mixer
from pygame.locals import *
import tkinter as tk
import subprocess

# Inicializar pygame
pygame.init()

# Configuración de la ventana del juego
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game Clasico")

# Colores
green = (0, 128, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
purple = (128, 0, 128)
yellow = (255, 255, 0)

# Tamaño de los segmentos del gusano y velocidad
segment_size = 20
segment_speed = 20

clock = pygame.time.Clock()

def game_loop():
    game_over = False
    game_exit = False
    
    # Cargar la música de fondo
    pygame.mixer.music.load("Plants vs. Zombies (Main Theme).mp3")

    # Configurar el volumen inicial de la música
    pygame.mixer.music.set_volume(0.1)  # Ajusta el volumen entre 0.0 y 1.0 según tus preferencias

    # Reproducir la música de fondo en bucle infinito
    pygame.mixer.music.play(loops=-1)
    
    # Cargar el sonido de comer pou
    eating_sound = pygame.mixer.Sound("Pou eating sound effect.mp3")
    
    # Cargar el sonido de "Game Over"
    game_over_sound = pygame.mixer.Sound("Game Over Sound Effects High Quality.mp3")

    # Establecer el volumen inicial del sonido game over
    volumen = 0.1  # Valor de ejemplo
    pygame.mixer.music.set_volume(volumen)

    game_over_sound_played = False
    
    # Función para abrir el menú
    def open_menu():
        pygame.quit()
        subprocess.Popen(["python", "inicio.py"])
        quit()

    # Posición inicial del gusano
    head_x = window_width / 2
    head_y = window_height / 2

    # Inicializar el gusano como una lista de segmentos
    segments = [(head_x, head_y)]
    for _ in range(2):
        segments.append((segments[-1][0] - segment_size, segments[-1][1]))

    # Generar una posición aleatoria para la manzana
    apple_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
    apple_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
    
    # Generar una posición aleatoria para la uva
    grape_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
    grape_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
    

    # Variables para controlar la dirección y velocidad del gusano
    change_x = segment_size
    change_y = 0
    last_key = pygame.K_RIGHT
    
    # Puntaje inicial del jugador
    score = 0

    # Tamaño de la fuente para el texto "Game Over"
    font_size_game_over = 100

    # Fuente para el texto "Game Over"
    font_game_over = pygame.font.SysFont(None, font_size_game_over)
    
    # Variables para controlar la animación de parpadeo
    fade_alpha = 255
    fade_dir = -1
    fade_speed = 0.05  # Ajusta la velocidad del parpadeo (menor valor = más lento)
    
    # Tamaño de la fuente para el "Score"
    font_size_score = 50

    # Fuente para el texto "Score"
    font_size_score = pygame.font.SysFont(None, font_size_score)
    
    # Tamaño de la fuente para los mensajes adicionales (salir y volver a jugar)
    font_size_message = 30

    # Fuente para los mensajes adicionales (salir y volver a jugar)
    font_message = pygame.font.SysFont(None, font_size_message)

    # Fuente para el puntaje
    font = pygame.font.SysFont(None, 30)

    while not game_exit:
        while game_over:
            # Pantalla de game over
            window.fill(black)
            
            # Renderizar el texto "Game Over" en una superficie transparente
            text_game_over_surface = font_game_over.render("Game Over", True, red)
            text_game_over_surface.set_alpha(fade_alpha)
            window.blit(text_game_over_surface, (window_width / 2 - text_game_over_surface.get_width() / 2, window_height / 2 - text_game_over_surface.get_height() / 2))
            
            # Renderizar el puntaje en la pantalla de Game Over
            text_score = font_size_score.render(f"Puntaje total: {score}", True, white)
            window.blit(text_score, (window_width / 2 - text_score.get_width() / 2, window_height / 2 - text_game_over_surface.get_height() / 2 + 70))
            
            # Renderizar el los dos mensajes adicionales (salir / volver a jugar)
            text_quit_message = font_message.render('Presione "q" para salir', True, white)
            text_restart_message = font_message.render('Presione "r" para volver a jugar', True, white)
            window.blit(text_quit_message, (window_width / 2 - text_quit_message.get_width() / 2, window_height / 2 + text_game_over_surface.get_height() / 2 + 50))
            window.blit(text_restart_message, (window_width / 2 - text_restart_message.get_width() / 2, window_height / 2 + text_game_over_surface.get_height() / 2 + 50 + font_size_message))
            
            # Ubicación personalizada del botón en píxeles
            button_x = 300
            button_y = 500

            # Dimensiones del botón
            button_width = 200
            button_height = 50

            # Código para dibujar el botón y su texto
            pygame.draw.rect(window, white, (button_x, button_y, button_width, button_height))
            button_text = font_message.render('Volver al Menú', True, black)
            button_text_x = button_x + button_width // 2 - button_text.get_width() // 2
            button_text_y = button_y + button_height // 2 - button_text.get_height() // 2
            window.blit(button_text, (button_text_x, button_text_y))
            
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + button_height:
                pygame.draw.rect(window, green, (button_x, button_y, button_width, button_height))
                button_text = font_message.render('Volver al Menú', True, white)
                window.blit(button_text, (button_text_x, button_text_y))
                if pygame.mouse.get_pressed()[0]:
                    open_menu()
            
            pygame.display.update()
            
            # Detener la música de fondo al mostrar el mensaje de "Game Over"
            pygame.mixer.music.stop()
            
            # Reproducir el sonido de "Game Over" si no se ha reproducido antes
            if not game_over_sound_played:
                game_over_sound.play()
                game_over_sound_played = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_exit = True
                    elif event.key == pygame.K_r:
                        # Detener el sonido de "Game Over"
                        pygame.mixer.Sound.stop(game_over_sound)
                        # Se reiniciara el juego
                        game_loop()
            
            # Animación de parpadeo con desvanecido
            fade_alpha += fade_dir * fade_speed
            if fade_alpha <= 0:
                fade_alpha = 0
                fade_dir = 1
            elif fade_alpha >= 255:
                fade_alpha = 255
                fade_dir = -1

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
        
        # Verificar si el gusano chocó consigo mismo
        if (head_x, head_y) in segments[:-1]:
            game_over = True
            print("Me he chocado conmigo mismo")

        # Verificar si el gusano chocó contra los bordes de la ventana
        if head_x >= window_width or head_x < 0 or head_y >= window_height or head_y < 0:
            game_over = True
            print("Me he chocado con el borde")

        # Actualizar la ventana
        window.fill(black)

        # Dibujar el gusano
        for segment in segments:
            pygame.draw.rect(window, green, (segment[0], segment[1], segment_size, segment_size))

        # Dibujar el punto (manzana)
        pygame.draw.rect(window, red, (apple_x, apple_y, segment_size, segment_size))
        
        # Dibujar el punto (uva)
        pygame.draw.rect(window, purple, (grape_x, grape_y, segment_size, segment_size))

        # Agregar la nueva posición de la cabeza del gusano a la lista de segmentos
        segments.append((head_x, head_y))

        # Verificar si el gusano alcanzó el punto (manzana) o la uva
        if head_x == apple_x and head_y == apple_y:
            print("He comido una manzana")
            # Reproducir sonido de gusando comiendo
            eating_sound.play()
            # Generar una nueva posición aleatoria para la manzana
            while (apple_x, apple_y) in segments:
                apple_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
                apple_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
            # Incrementar el puntaje
            score += 1

        elif head_x == grape_x and head_y == grape_y:
            print("He comido una uva")
            # Reproducir sonido de gusando comiendo
            eating_sound.play()
            # Generar una nueva posición aleatoria para la uva
            while (grape_x, grape_y) in segments or (grape_x == apple_x and grape_y == apple_y):
                grape_x = round(random.randrange(0, window_width - segment_size) / segment_size) * segment_size
                grape_y = round(random.randrange(0, window_height - segment_size) / segment_size) * segment_size
            # Incrementar el puntaje
            score += 3
            # Obtener la posición del último segmento del gusano
            last_segment_x, last_segment_y = segments[-1]
            # Agregar 3 segmentos al gusano en la posición del último segmento
            for _ in range(3):
                segments.append((last_segment_x, last_segment_y))
        else:
            # Si no se alcanzó el punto, eliminar el último segmento del gusano
            segments.pop(0)

        

        # Dibujar el puntaje en la esquina superior derecha
        score_text = font.render(f"Puntaje: {score}", True, white)
        window.blit(score_text, (window_width - score_text.get_width() - 10, 10))

        pygame.display.update()
        clock.tick(10)  # Velocidad del juego (10 cuadros por segundo)

    pygame.quit()
    quit()

game_loop()
