import tkinter as tk
from tkinter import messagebox
import os
import pygame
from datetime import datetime

# Fecha de vencimiento del programa (cambiar según sea necesario)
fecha_vencimiento = datetime(2023, 12, 25) # YY/MM/DD

# Verifica si el programa ha caducado
if datetime.now() > fecha_vencimiento:
    # Crea una ventana emergente para informar al usuario que el programa ha caducado
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Programa caducado", "Este programa ha caducado, contactece con el administrador, Gmail: fcastillosanabria@gmail.com.")
    os._exit(0)

# Función para abrir el juego en una nueva ventana
def open_game():
    root.destroy()
    pygame.mixer.music.stop()
    os.system("python juego.py")
    os._exit(0)
    
# Función para abrir el juego de dos perosnas en una nueva ventana
def open_game2Player():
    root.destroy()
    pygame.mixer.music.stop()
    os.system("python juego2Player.py")
    os._exit(0)

# Función para salir del programa
def exit_program():
    confirm = messagebox.askyesno("Salir", "¿Estás seguro que deseas salir?")
    if confirm:
        pygame.mixer.quit()
        os._exit(0)

# Crear la ventana principal
root = tk.Tk()
root.title("Snake Game VG 2023")  # Colocar nombre a la ventana actual
window_width = 800  # Ancho de la ventana
window_height = 600  # Altura de la ventana
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="orange")  # Establecer el color de fondo de la ventana
root.resizable(0, 0)  # Desactivar la opción de maximizar la ventana

# Botón para abrir el juego
game_button = tk.Button(root, text="Clasico", command=open_game)
game_button.pack()

game_button = tk.Button(root, text="Multijugador", command=open_game2Player)
game_button.pack()

exit_button = tk.Button(root, text="Salir", command=exit_program)
exit_button.pack(side="bottom", pady=10)

# Reproducir música
music_file = "Can_I_Call_You_Tonight.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)  # El -1 indica que se reproduzca en bucle

# Configurar el cierre de la ventana
root.protocol("WM_DELETE_WINDOW", exit_program)

# Mostrar la ventana
root.mainloop()
