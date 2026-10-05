# Pre-Entrega QA Automation: SauceDemo

Proyecto de automatización de pruebas integrales sobre la plataforma [SauceDemo](https://www.saucedemo.com/), desarrollado con **Python**, **Selenium WebDriver** y **Pytest**.

---

## 🎯 Propósito del Proyecto

El objetivo de este proyecto es automatizar flujos clave de usuario y validar componentes funcionales de la aplicación web SauceDemo mediante dos enfoques complementarios:
1. **Scripts introductorios de aprendizaje (`selenium/`)**: Demostración procedural y secuencial de interacciones básicas con WebDriver.
2. **Suite formal de pruebas (`tests/`)**: Framework robusto y escalable basado en Pytest con fixtures, esperas explícitas, aserciones declarativas y reportes HTML.

---

## 🛠️ Tecnologías y Dependencias

- **Python 3.10+**: Lenguaje de desarrollo principal.
- **Selenium WebDriver 4+**: Automatización e interacción con el navegador web.
- **Pytest 8+**: Framework para la estructuración y ejecución de pruebas.
- **pytest-html**: Generación de reportes interactivos y autónomos en formato HTML.
- **webdriver-manager**: Administración y resolución automática de binarios de ChromeDriver.
- **Git & GitHub**: Control de versiones con historial colaborativo y conventional commits.

---

## 📁 Estructura del Proyecto

```text
prentregaLFC26221/
├── reports/
│   ├── screenshots/          # Capturas automáticas en caso de fallos
│   └── reporte.html          # Reporte autónomo de ejecución de Pytest
├── selenium/                 # Scripts secuenciales de aprendizaje
│   ├── actividad_1_login.py      # Actividad 1: Automatización de login y validación
│   ├── actividad_2_inventario.py # Actividad 2: Inspección de catálogo e inventario
│   └── actividad_3_carrito.py    # Actividad 3: Flujo de carrito de compras
├── tests/                    # Suite estructurada con Pytest
│   ├── conftest.py           # Fixture de sesión de driver y hook de evidencias
│   └── test_saucedemo.py     # 5 casos de prueba automatizados
├── utils/
│   └── helpers.py            # Funciones auxiliares y esperas explícitas (WebDriverWait)
├── pytest.ini                # Configuración de pytest, rutas y marcadores
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación técnica del proyecto
```

---

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/ero629222/prentrega26221.git
   cd prentregaLFC26221
   ```

2. **Crear y activar el entorno virtual**:
   - En Windows (PowerShell / CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - En Linux / macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Guía de Ejecución

### 1. Ejecución de Scripts de Aprendizaje (`selenium/`)
Puedes ejecutar de forma independiente cada una de las actividades prácticas:
```bash
python selenium/actividad_1_login.py
python selenium/actividad_2_inventario.py
python selenium/actividad_3_carrito.py
```

### 2. Ejecución de la Suite Pytest (`tests/`)
Para ejecutar todas las pruebas automatizadas con salida detallada:
```bash
pytest -v
```

Para filtrar por tipo de prueba utilizando marcadores:
- **Smoke Tests** (flujos críticos rápidos):
  ```bash
  pytest -m smoke
  ```
- **Regression Tests** (catálogo, validaciones negativas y sesión):
  ```bash
  pytest -m regression
  ```

### 3. Generación de Reporte HTML
La configuración predefinida en `pytest.ini` genera automáticamente el reporte tras cada ejecución:
```bash
# El reporte se guarda en reports/reporte.html
pytest
```
El reporte incluye métricas de tiempo, resultados por caso de prueba y detalles de entorno.

---

## ✅ Casos de Prueba Implementados

| ID | Función de Prueba | Marcador | Descripción |
| :--- | :--- | :--- | :--- |
| **CP01** | `test_login_exitoso` | `@pytest.mark.smoke` | Valida inicio de sesión exitoso con credenciales estándar y redirección a `inventory.html`. |
| **CP02** | `test_navegacion_y_catalogo` | `@pytest.mark.regression` | Verifica visibilidad del menú hamburguesa, filtro de ordenamiento y presencia de ítems en catálogo. |
| **CP03** | `test_interaccion_carrito_compras` | `@pytest.mark.smoke` | Agrega un producto, valida el incremento del badge a '1' y comprueba su inclusión en el carrito. |
| **CP04** | `test_login_credenciales_invalidas` | `@pytest.mark.regression` | Verifica el mensaje de error apropiado ante credenciales erróneas. |
| **CP05** | `test_cierre_de_sesion` | `@pytest.mark.regression` | Abre el menú lateral, ejecuta logout y comprueba el retorno al formulario de login. |

---

## ✨ Buenas Prácticas Aplicadas

- **Esperas Explícitas (`WebDriverWait`)**: Control de asincronía en React mediante `visibility_of_element_located` y `element_to_be_clickable`, eliminando pausas arbitrarias (`sleep`).
- **Gestión Automatizada de Drivers**: Integración de `webdriver-manager` para asegurar compatibilidad continua del navegador sin descargas manuales.
- **Aislamiento de Pruebas**: Cada caso de prueba inicia y cierra una sesión limpia del navegador mediante la fixture `@pytest.fixture` en `conftest.py`.
- **Captura Automática de Evidencias**: Implementación del hook `pytest_runtest_makereport` para guardar screenshots automáticos con marca de tiempo ante fallos.
- **Historial de Commits Convencionales**: Uso del estándar Conventional Commits (`feat:`, `chore:`, `docs:`) para trazabilidad colaborativa en Git.

---

## 👤 Autor
- **Alumno**: Leo
- **Curso**: Automatización de Testing QA - Comisión 26221