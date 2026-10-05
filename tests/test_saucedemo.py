"""
Suite de pruebas automatizadas sobre SauceDemo.
Cobertura de Clases 6 a 8: Login, Catálogo, Interacción con Carrito y Sesión.
"""
import pytest
from selenium.webdriver.common.by import By
from utils.helpers import (
    esperar_elemento_visible,
    esperar_elemento_clickable,
    esperar_url_contenga,
)

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

    # Validaciones obligatorias
    assert esperar_url_contenga(driver, "inventory.html"), "Error: No redirigio a inventory.html"
    
    titulo = esperar_elemento_visible(driver, By.CLASS_NAME, "title").text
    assert titulo.lower() == "products", f"Se esperaba 'Products' y se obtuvo: {titulo}"
    
    logo = esperar_elemento_visible(driver, By.CLASS_NAME, "app_logo").text
    assert logo == "Swag Labs", f"Se esperaba 'Swag Labs' y se obtuvo: {logo}"


@pytest.mark.regression
def test_navegacion_y_catalogo(driver):
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


@pytest.mark.smoke
def test_interaccion_carrito_compras(driver):
    """CP03: Agregar primer producto, verificar contador y comprobarlo dentro del carrito."""
    ejecutar_login(driver)

    # Localizar primer item y guardar su nombre
    primer_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre_esperado = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Añadir al carrito
    primer_item.find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]").click()

    # Validar que el badge del carrito sea '1'
    badge = esperar_elemento_visible(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1", f"El badge esperaba '1' y muestra: {badge.text}"

    # Navegar al carrito y verificar presencia
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert esperar_url_contenga(driver, "cart.html"), "Fallo la navegacion a cart.html"

    items_carrito = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    nombres_en_carrito = [elem.text for elem in items_carrito]
    assert nombre_esperado in nombres_en_carrito, f"El producto {nombre_esperado} no esta en el carrito"


@pytest.mark.regression
def test_login_credenciales_invalidas(driver):
    """CP04: Validar mensaje de error ante intento de login con credenciales invalidas."""
    driver.get(URL_LOGIN)
    esperar_elemento_visible(driver, By.ID, "user-name").send_keys("invalid_user")
    esperar_elemento_visible(driver, By.ID, "password").send_keys("invalid_password")
    esperar_elemento_visible(driver, By.ID, "login-button").click()

    mensaje_error = esperar_elemento_visible(driver, By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in mensaje_error, (
        f"El mensaje de error esperado no coincide. Obtenido: '{mensaje_error}'"
    )


@pytest.mark.regression
def test_cierre_de_sesion(driver):
    """CP05: Validar flujo de cierre de sesion y retorno a la pantalla principal."""
    ejecutar_login(driver)

    # Abrir menu lateral hamburguesa
    esperar_elemento_clickable(driver, By.ID, "react-burger-menu-btn").click()

    # Esperar y hacer clic en enlace de logout
    enlace_logout = esperar_elemento_clickable(driver, By.ID, "logout_sidebar_link")
    enlace_logout.click()

    # Validar retorno a pantalla de login y presencia de formulario
    boton_login = esperar_elemento_visible(driver, By.ID, "login-button")
    assert boton_login.is_displayed(), "No se visualiza el boton de login tras cerrar sesion"
    assert "inventory.html" not in driver.current_url, (
        "El usuario permanece en el inventario tras cerrar sesion"
    )