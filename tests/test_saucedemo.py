import pytest
from selenium.webdriver.common.by import By
from utils.helpers import esperar_elemento_visible, esperar_url_contenga

URL_LOGIN = "https://www.saucedemo.com/"

def ejecutar_login(driver, usuario="standard_user", password="secret_sauce"):
    """Helper interno para login seguro con teclado real en campos de React."""
    driver.get(URL_LOGIN)
    esperar_elemento_visible(driver, By.ID, "user-name").send_keys(usuario)
    esperar_elemento_visible(driver, By.ID, "password").send_keys(password)
    esperar_elemento_visible(driver, By.ID, "login-button").click()
    esperar_url_contenga(driver, "inventory.html")

@pytest.mark.smoke
def test_login_exitoso(driver):
    """CP01: Validar login con credenciales estandar y redireccion al inventario."""
    driver.get(URL_LOGIN)
    
    esperar_elemento_visible(driver, By.ID, "user-name").send_keys("standard_user")
    esperar_elemento_visible(driver, By.ID, "password").send_keys("secret_sauce")
    esperar_elemento_visible(driver, By.ID, "login-button").click()

    # Criterios obligatorios: URL y titulos
    assert esperar_url_contenga(driver, "inventory.html"), "Error: No redirigio a inventory.html"
    
    titulo = esperar_elemento_visible(driver, By.CLASS_NAME, "title").text
    assert titulo.lower() == "products", f"Se esperaba 'Products' y se obtuvo: {titulo}"
    
    logo = esperar_elemento_visible(driver, By.CLASS_NAME, "app_logo").text
    assert logo == "Swag Labs", f"Se esperaba 'Swag Labs' y se obtuvo: {logo}"