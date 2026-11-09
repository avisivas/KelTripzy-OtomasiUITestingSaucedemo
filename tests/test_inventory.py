import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_backpack_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()

    assert inventory.get_cart_badge_count() == "1"


def test_logout_from_inventory(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.login("standard_user", "secret_sauce")
    inventory.logout()

    assert inventory.is_login_button_displayed()