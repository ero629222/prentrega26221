import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import tomar_captura

@pytest.fixture(scope="function")
def driver():
    """Fixture que inicializa y cierra una sesion limpia de Chrome por cada test."""
    opciones = Options()
    opciones.add_argument("--start-maximized")
    opciones.add_argument("--disable-notifications")

    servicio = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=servicio, options=opciones)

    yield _driver

    _driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Toma captura automatica si un test falla durante su ejecucion."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            nombre_test = item.name
            tomar_captura(driver, f"FALLO_{nombre_test}")