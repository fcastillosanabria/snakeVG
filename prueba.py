import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Ruta del controlador del navegador Microsoft Edge (no es necesario en este caso)
edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'

# URL de la página de inicio de sesión de Yanbal Perú
yanbal_url = 'https://j6.yanbalperu.com/portaldenegocio/login?ExternalAuth=1'

# Rellenar con tu número de consultora y contraseña
tu_numero_de_consultora = '112297880'
tu_contrasena = 'Shumy1972'

try:
    # Crear una instancia de EdgeOptions y agregar el User-Agent
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    # Inicializar el navegador Microsoft Edge con las opciones modificadas
    driver = webdriver.Edge(options=edge_options)
    driver.get(yanbal_url)

    # Esperar un momento para que la página esté completamente cargada
    time.sleep(5)

    # Encontrar el campo de usuario y llenarlo automáticamente
    numero_consultora_input = driver.find_element(By.ID, 'UserName')
    numero_consultora_input.send_keys(tu_numero_de_consultora)

    # Utilizar WebDriverWait para esperar a que el campo de contraseña esté visible y luego llenarlo
    wait = WebDriverWait(driver, 10)
    contrasena_input = wait.until(EC.visibility_of_element_located((By.ID, 'Password')))

    # Agregar una pausa antes de enviar la contraseña
    time.sleep(2)

    contrasena_input.send_keys(tu_contrasena)

    # Simular la pulsación de tecla "Enter" después de llenar la contraseña
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Esperar un momento para que se complete el inicio de sesión y se cargue el dashboard
    time.sleep(random.uniform(5, 10))  # Pausa de 5 a 10 segundos

    # Esperar la entrada del usuario antes de cerrar el navegador
    input("Presiona cualquier tecla para cerrar el navegador...")
    # driver.quit()

except Exception as e:
    # Si ocurre algún error, imprimimos el mensaje de error y cerramos el navegador.
    print(f"Ocurrió un error: {e}")
    driver.quit()
