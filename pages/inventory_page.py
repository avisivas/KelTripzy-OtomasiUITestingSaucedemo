from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    """Page Object untuk halaman Inventory dan Cart SauceDemo."""

    ADD_TO_CART_BACKPACK = (
        By.XPATH,
        "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    )

    CART_BADGE = (
        By.XPATH,
        "//span[@class='shopping_cart_badge']"
    )

    BURGER_MENU = (
        By.ID,
        "react-burger-menu-btn"
    )

    LOGOUT_LINK = (
        By.ID,
        "logout_sidebar_link"
    )

    LOGIN_BUTTON = (
        By.ID,
        "login-button"
    )

    def add_backpack_to_cart(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BACKPACK)
        )
        element.click()

    def get_cart_badge_count(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return element.text

    def logout(self):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.element_to_be_clickable(self.BURGER_MENU)
        ).click()

        wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()

    def is_login_button_displayed(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOGIN_BUTTON)
            ).is_displayed()
        except Exception:
            return False