"""
actividad_1_login.py
Automatiza el login en Sauce Demo y valida la URL y el título.
Actividad práctica introductoria de Selenium WebDriver.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1) Crear el driver con opciones limpias
opciones = webdriver.ChromeOptions()
opciones.add_argument("--start-maximized")
#opciones.add_argument("--headless=new")

servicio = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servicio, options=opciones)
driver.implicitly_wait(5)  # espera implícita para todos los find_element

try:
    print("[Actividad 1] Iniciando prueba de Login...")
    # 2) Abrir la pantalla de login
    driver.get("https://www.saucedemo.com")

    # 3) Completar usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 4) Enviar formulario
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # 5) Verificar redirección a /inventory.html
    assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"

    # Reto extra
    assert driver.title == "Swag Labs", "Titulo inesperado"

    print("[OK] [Actividad 1] Test OK: Login exitoso, redireccion y titulo validados correctamente.")
finally:
    # 6) Cerrar el navegador
    driver.quit()

