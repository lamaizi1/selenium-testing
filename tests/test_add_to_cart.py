from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.screenshot


def test_add_to_cart(driver):

    wait = WebDriverWait(driver, 10)

    # Ouvrir SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Connexion
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Attendre que la page Products soit chargée
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    # Ajouter le produit au panier
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()

    # Ouvrir le panier
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    try:
        product = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        assert product.text == "Sauce Labs Backpack"

        utils.screenshot.take_screenshot(
            driver,
            "add_to_cart_success"
        )

    except Exception:
        utils.screenshot.take_screenshot(
            driver,
            "add_to_cart_failed"
        )
        raise