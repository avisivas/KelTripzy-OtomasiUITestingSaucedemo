from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="function")
def driver():
    """Inisialisasi browser Google Chrome untuk setiap pengujian."""

    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    # Membuka halaman login SauceDemo
    driver.get("https://www.saucedemo.com/")

    yield driver

    # Menutup browser setelah pengujian selesai
    driver.quit()