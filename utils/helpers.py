import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_elemento_visible(driver, by, locator, timeout=10):
    """Espera explicita para evitar bloqueos por carga asincrona o React."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    )

def esperar_url_contenga(driver, fragmento, timeout=10):
    """Espera explicita para validar cambios en la URL."""
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(fragmento)
    )

def tomar_captura(driver, nombre_archivo="evidencia"):
    """Guarda una captura de pantalla en la carpeta reports/screenshots/."""
    carpeta = os.path.join("reports", "screenshots")
    os.makedirs(carpeta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(carpeta, f"{nombre_archivo}_{timestamp}.png")
    driver.save_screenshot(ruta)
    return ruta