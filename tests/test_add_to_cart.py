from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.screenshot

# Lancer Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Ouvrir SauceDemo
driver.get("https://www.saucedemo.com/")

# Attente explicite
wait = WebDriverWait(driver, 10)

# Connexion
wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
).send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

try:
    # Vérifier que le produit est présent
    product = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )

    # Vérifier que le bon produit est affiché
    assert product.text == "Sauce Labs Backpack"

    print("✅ Test Passed : Produit ajouté au panier avec succès.")

    # Capture d'écran en cas de succès
    utils.screenshot.take_screenshot(driver, "add_to_cart_success")

except Exception as e:
    print("❌ Test Failed")

    # Capture d'écran en cas d'échec
    utils.screenshot.take_screenshot(driver, "add_to_cart_failed")

    print(e)

finally:
    # Fermer le navigateur dans tous les cas
    driver.quit()