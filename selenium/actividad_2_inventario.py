"""
actividad_2_inventario.py
Valida el título 'Products' y muestra el primer producto (nombre y precio).
Actividad práctica 2 de Selenium WebDriver.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opciones = webdriver.ChromeOptions()
opciones.add_argument("--start-maximized")
# opciones.add_argument("--headless=new")  # Descomentar si se desea  la ejecucion sin ventana

servicio = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servicio, options=opciones)
driver.implicitly_wait(5)

try:
    print("[Actividad 2] Iniciando validacion de Inventario y Catalogo...")
    # Login rapido (mismo flujo que la actividad 1)
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    # 1) Validar titulo de la pagina de inventario
    header_title = driver.find_element(
        By.CSS_SELECTOR, "div.header_secondary_container .title"
    ).text
    assert header_title == "Products", f"Titulo inesperado: {header_title}"

    # 2) Verificar que exista al menos un producto
    products = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(products) > 0, "No se encontraron productos"

    # 3) Capturar nombre y precio del primer producto
    first_name = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    first_price = products[0].find_element(By.CSS_SELECTOR, ".inventory_item_price").text
    print(f"Primer producto detectado -> {first_name} - {first_price}")

    print("[OK] [Actividad 2] Test OK: Catalogo e inventario validados correctamente.")
finally:
    driver.quit()

