
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Kelas dasar yang diwarisi oleh seluruh halaman Page Object."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        """Mencari elemen menggunakan explicit wait."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(
                f"Elemen dengan lokator {locator} "
                "tidak ditemukan atau tidak terlihat."
            )

    def click(self, locator):
        """Menunggu elemen dapat diklik kemudian melakukan klik."""
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            raise TimeoutException(
                f"Elemen dengan lokator {locator} "
                "tidak dapat diklik dalam waktu tunggu."
            )

    def type_text(self, locator, text):
        """Mengisi teks ke input setelah membersihkan isinya."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Mengambil teks dari elemen."""
        return self.find_element(locator).text

    def get_current_url(self):
        """Mengambil URL halaman saat ini."""
        return self.driver.current_url

    def is_element_visible(self, locator):
        """Memeriksa apakah elemen terlihat."""
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False