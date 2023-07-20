import os
import pygame
from datetime import datetime
from PIL import Image

# Fecha de vencimiento del programa (cambiar según sea necesario)
fecha_vencimiento = datetime(2023, 12, 25) # YY/MM/DD

# Verifica si el programa ha caducado
if datetime.now() > fecha_vencimiento:
    # Crea una ventana emergente para informar al usuario que el programa ha caducado
    pygame.init()
    pygame.display.set_caption("Programa caducado")
    window_size = (700, 250)
    window = pygame.display.set_mode(window_size)
    font = pygame.font.SysFont(None, 30)
    text_surface = font.render("Este programa ha caducado. :(((", True, (255, 0, 0))
    text_contac = font.render("Cantactame:", True, (255, 255, 255))
    text_Email = font.render("Email: fcastillosanabria@gmail.com", True, (255, 255, 255))
    text_Ig = font.render("Instagram: franciscastillo.69", True, (255, 255, 255))
    text_Ws = font.render("WhatsApp: 934 179 705", True, (255, 255, 255))
    window.blit(text_surface, (50, 50))
    window.blit(text_contac, (50, 100))
    window.blit(text_Email, (50, 130))
    window.blit(text_Ig, (50, 160))
    window.blit(text_Ws, (50, 190))
    pygame.display.update()

    # Bucle para mantener la ventana abierta
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
else:
    # Función para abrir el juego en una nueva ventana
    def open_game():
        pygame.mixer.music.stop()
        os.system("python juego.py")
        pygame.quit()
        os._exit(0)
    
    # Función para abrir el juego de dos jugadores en una nueva ventana
    def open_game2Player():
        pygame.mixer.music.stop()
        os.system("python juego2Player.py")
        pygame.quit()
        os._exit(0)

    # Función para salir del programa
    def exit_program():
        confirm = pygame.messagebox.askyesno("Salir", "¿Estás seguro que deseas salir?")
        if confirm:
            pygame.quit()
            os._exit(0)

    # Inicializar Pygame
    pygame.init()

    # Crear la ventana principal
    window_width = 800  # Ancho de la ventana
    window_height = 600  # Altura de la ventana
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Snake Game VG 2023")

    # Cargar la imagen
    image_path = "logoSnake.png"
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (400, 150))

    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)

        # Rellenar la ventana con un color de fondo transparente
        window.fill((0, 255, 0, 0))

        # Mostrar la imagen en la ventana
        image_rect = image.get_rect(center=(window_width // 2, window_height // 2 - 150))
        window.blit(image, image_rect)

        # Botón para Clásico
        button_width = 300
        button_height = 50
        button_x = window_width // 2 - button_width // 2
        button_y = 280
        pygame.draw.rect(window, (255, 255, 255), (button_x, button_y, button_width, button_height))
        font = pygame.font.SysFont(None, 40)
        text_surface = font.render("Clásico", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        window.blit(text_surface, text_rect)

        # Botón para Multijugador
        button_y += 100
        pygame.draw.rect(window, (255, 255, 255), (button_x, button_y, button_width, button_height))
        text_surface = font.render("Multijugador", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        window.blit(text_surface, text_rect)

        # Botón para Salir
        button_y += 100
        pygame.draw.rect(window, (255, 255, 255), (button_x, button_y, button_width, button_height))
        text_surface = font.render("Salir", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        window.blit(text_surface, text_rect)

        # Actualizar la ventana
        pygame.display.update()

        # Detectar clics en los botones
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]:
            if button_x <= mouse_pos[0] <= button_x + button_width:
                if 280 <= mouse_pos[1] <= 280 + button_height:
                    open_game()
                elif 380 <= mouse_pos[1] <= 380 + button_height:
                    open_game2Player()
                elif 480 <= mouse_pos[1] <= 480 + button_height:
                    exit_program()
