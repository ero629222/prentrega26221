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
    
    @pytest.mark.regression
def test_navegacion_y_catalogo(driver):s
    """CP02: Validar visibilidad de elementos UI y detalle del primer producto del catalogo."""
    ejecutar_login(driver)

    # Validar presencia de controles principales de interfaz
    menu = esperar_elemento_visible(driver, By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menu principal no se encuentra visible"

    filtro = esperar_elemento_visible(driver, By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro de ordenamiento no se encuentra visible"

    # Validar presencia de catalogo y listar nombre/precio del primero
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0, "No se encontraron productos en el inventario"

    primer_item = items[0]
    nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert len(nombre) > 0, "El nombre del primer producto esta vacio"
    assert "$" in precio, f"El precio '{precio}' no contiene formato de moneda"
    print(f"\n[CATALOGO] Primer producto detectado: {nombre} | Precio: {precio}")